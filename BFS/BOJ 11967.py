from collections import deque
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
data=list(list(list() for _ in range(n+1)) for _ in range(n+1))
visited=[list(0 for _ in range(n+1)) for _ in range(n+1)]
light=list(list(0 for _ in range(n+1)) for _ in range(n+1))
light[1][1]=1
for _ in range(m):
    x,y,a,b=map(int,input().split())
    data[x][y].append([a,b])
dx=[-1,0,0,1]
dy=[0,-1,1,0]
q=deque()
q.append([1,1])
while q:
    x,y=q.popleft()
    for i,j in data[x][y]:
        light[i][j]=1
        if visited[i][j]:
            continue
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<nx<=n and 0<ny<=n and light[nx][ny] and visited[nx][ny]:
                q.append([i,j])
                visited[i][j]=1
                break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<nx<=n and 0<ny<=n and not visited[nx][ny]:
            if light[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny]=1
answer=sum(light[i].count(1) for i in range(n+1))
print(answer)