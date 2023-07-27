import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
visited=[[0 for _ in range(m)] for _ in range(n)]
start=0
answer=[[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j]==2:
            start=[i,j]
            answer[i][j]=0
        elif data[i][j]==0:
            answer[i][j]=0
dx=[[0,1],[0,-1],[1,0],[-1,0]]
q=deque()
q.append(start)
visited[start[0]][start[1]]=1

while q:
    x,y=q.popleft()
    for a,b in dx:
        if 0<=x+a<n and 0<=y+b<m and data[x+a][y+b]==1 and not visited[x+a][y+b]:
            visited[x+a][y+b]=1
            q.append([x+a,y+b])
            answer[x+a][y+b]=answer[x][y]+1

for i in range(n):
    print(*answer[i])