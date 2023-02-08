from collections import deque
import heapq
n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
q=[[data[0][0],0,0]]
answer=[[1e10]*m for _ in range(n)]
dx=[[0,1],[0,-1],[1,0],[-1,0]]
answer[0][0]=0
while q:
    val,x,y=heapq.heappop(q)
    for a,b in dx:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and data[nx][ny]!=-1:
            if answer[nx][ny]>val+data[nx][ny]:
                answer[nx][ny]=val+data[nx][ny]
                heapq.heappush(q,[answer[nx][ny],nx,ny])
if answer[n-1][m-1]==1e10 or data[0][0]==-1:
    print(-1)
else:
    print(answer[n-1][m-1])
