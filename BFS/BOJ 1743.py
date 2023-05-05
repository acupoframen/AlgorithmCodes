import sys
input=sys.stdin.readline
from collections import deque
n,m,k=map(int,input().split())
data=[[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    data[a][b]=1

dx=[[-1,0],[0,-1],[0,1],[1,0]]
answer=0
def bfs(a,b):
    size=0
    q=deque()
    q.append([a,b])
    data[a][b]=0
    while q:
        size+=1
        a,b=q.popleft()
        for i in range(4):
            if 0<a+dx[i][0]<n+1 and 0<b+dx[i][1]<m+1 and data[a+dx[i][0]][b+dx[i][1]]==1:
                data[a+dx[i][0]][b+dx[i][1]]=0
                q.append([a+dx[i][0],b+dx[i][1]])
    return size
for i in range(1,n+1):
    for j in range(1,m+1):
        if data[i][j]==1:
            answer=max(answer,bfs(i,j))
print(answer)