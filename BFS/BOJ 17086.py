from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,1,0,-1,1,-1,0,1]
answer=0

def f(i,j):
    q=deque()
    q.append((i,j,0))
    visited=list(list(0 for _ in range(m)) for _ in range(n))
    visited[i][j]=1
    while q:
        x,y,dist=q.popleft()
        for k in range(8):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if data[nx][ny]:
                    return dist+1
                else:
                    q.append((nx,ny,dist+1))
                    visited[nx][ny]=1

for i in range(n):
    for j in range(m):
        if data[i][j]==0:
            answer=max(answer,f(i,j))
            
print(answer)