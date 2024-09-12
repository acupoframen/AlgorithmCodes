import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(map(int,input().strip())) for _ in range(m))
q=[]
visited=list(list(1e10 for _ in range(n)) for _ in range(m))
heapq.heappush(q,[0,0,0])
visited[0][0]=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]
while q:
    d,x,y=heapq.heappop(q)
    if x==m-1 and y==n-1:
        print(d)
        break
    if visited[x][y]<d:
        continue
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<m and 0<=ny<n:
            if data[nx][ny] and d+1<visited[nx][ny]:
                visited[nx][ny]=d+1
                heapq.heappush(q,[d+1,nx,ny])
            elif not data[nx][ny] and d<visited[nx][ny]:
                visited[nx][ny]=d
                heapq.heappush(q,[d,nx,ny])