from collections import deque
n,m,k=map(int,input().split())
data=list(list(int(i) for i in input()) for _ in range(n))
visited=[[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
q=deque()
q.append([0,0,0,1]) #x,y, 깬 횟수, 거리
visited[0][0][0]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while q:
    x,y,b,dist=q.popleft()
    if x==n-1 and y==m-1:
        print(dist)
        break
    day=dist%2 
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if visited[nx][ny][b]==0 and data[nx][ny]==0:
            visited[nx][ny][b]=dist
            q.append([nx,ny,b,dist+1])
        elif b+1<=k and data[nx][ny]==1 and visited[nx][ny][b+1]==0:
            if day:
                visited[nx][ny][b+1]=dist
                q.append([nx,ny,b+1,dist+1])
            else:
                q.append([x,y,b,dist+1])
else:
    print(-1)