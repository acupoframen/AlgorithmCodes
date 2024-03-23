from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline

def bfs(virusList):
    global answer,blank
    tempblank=blank
    q=deque(virusList)
    temp=0
    visited=list(list(1e10 for _ in range(n)) for _ in range(n))
    for i,j in virusList:
        visited[i][j]=0
    while q:
        a,b=q.popleft()
        if answer<visited[a][b]:
            break
        for k in range(4):
            nx=a+dx[k]
            ny=b+dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==1e10:
                if data[nx][ny]==0:
                    tempblank-=1
                    q.append([nx,ny])
                    visited[nx][ny]=visited[a][b]+1
                    temp=max(temp,visited[nx][ny])
                elif data[nx][ny]==2:
                    q.append([nx,ny])
                    visited[nx][ny]=visited[a][b]+1
    if tempblank==0:
        return temp
    else:
        return 1e10
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
virus=[]
blank=0
for i in range(n):
    for j in range(n):
        if data[i][j]==2:
            virus.append([i,j])
        if data[i][j]==0:
            blank+=1

answer=1e10
for virusList in combinations(virus,m):
    answer=min(answer,bfs(virusList))

if answer==1e10:
    print(-1)
else:
    print(answer)