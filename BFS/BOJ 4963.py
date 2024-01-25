from collections import deque
dx=[-1,0,0,1,-1,-1,1,1]
dy=[0,1,-1,0,-1,1,-1,1]
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    data=[list(map(int,input().split())) for _ in range(b)]
    visited=[list(0 for _ in range(a)) for _ in range(b)]
    answer=0
    for i in range(b):
        for j in range(a):
            if visited[i][j]:
                continue
            if data[i][j]==0:
                visited[i][j]=1
                continue
            q=deque()
            q.append([i,j])
            answer+=1
            while q:
                x,y=q.popleft()
                visited[x][y]=1
                for k in range(8):
                    if 0<=x+dx[k]<b and 0<=y+dy[k]<a and not visited[x+dx[k]][y+dy[k]] and data[x+dx[k]][y+dy[k]]:
                        q.append([x+dx[k], y+dy[k]])
                        visited[x+dx[k]][y+dy[k]]=1
    print(answer)