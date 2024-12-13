from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,1,-1,0]

visited=list(list(0 for _ in range(m)) for _ in range(n))
answer=0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        q=deque()
        q.append([i,j])
        visited[i][j]=1
        flag=0
    
        while q:
            x,y=q.popleft()
            for k in range(8):
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<n and 0<=ny<m :
                    if data[x][y]<data[nx][ny]:
                        flag=1
                    elif not visited[nx][ny]:
                        if data[x][y]==data[nx][ny]:
                            q.append([nx,ny])
                            visited[nx][ny]=1
        if not flag:
            answer+=1
print(answer)