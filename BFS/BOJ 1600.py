import sys
import heapq
input=sys.stdin.readline
k=int(input())
w,h=map(int,input().split())
data= list(list(map(int,input().split())) for _ in range(h))
dist=list(list(list(1e10 for _ in range(w)) for _ in range(h)) for _ in range(k+1))
dist[0][0][0]=0
q=[]
heapq.heappush(q,[0,0,0,0]) #dist,k-use,x,y
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,2,-2,2,-2,-1,1]
oridx=[-1,1,0,0]
oridy=[0,0,-1,1]
while q:
    val,kuse,x,y=heapq.heappop(q)
    if val>dist[kuse][x][y]:
        continue
    if (x,y)==(h-1,w-1):
        print(val)
        exit(0)
    if kuse<k:
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and data[nx][ny]==0 and dist[kuse+1][nx][ny]>val+1:
                dist[kuse+1][nx][ny]=val+1
                heapq.heappush(q,[val+1,kuse+1,nx,ny])
    for i in range(4):
        nx=x+oridx[i]
        ny=y+oridy[i]
        if 0<=nx<h and 0<=ny<w and data[nx][ny]==0 and dist[kuse][nx][ny]>val+1:
            dist[kuse][nx][ny]=val+1
            heapq.heappush(q,[val+1,kuse,nx,ny])
print(-1)