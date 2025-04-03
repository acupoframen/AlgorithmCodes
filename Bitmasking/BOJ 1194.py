import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(input().strip()) for _ in range(n))
visited=list(list(list(0 for _ in range(2**6)) for _ in range(m)) for _ in range(n))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == "0":
            data[i][j] = "."
            q.append([i, j, 0])
            break

while q:
    x,y,key=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        currkey=key
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny]!='#' and not visited[nx][ny][currkey]:
                if data[nx][ny].isupper():
                    if not (key&1<<(ord(data[nx][ny])-ord("A"))):
                        continue
                elif data[nx][ny].islower():
                        currkey|=1<<(ord(data[nx][ny])-ord("a"))
                elif data[nx][ny]=="1":
                    print(visited[x][y][key]+1)
                    exit(0)
                q.append([nx,ny,currkey])
                visited[nx][ny][currkey]=visited[x][y][key]+1
print(-1)