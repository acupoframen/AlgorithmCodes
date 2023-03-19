import sys
input=sys.stdin.readline
import heapq
dx=[1,0,0,-1]
dy=[0,1,-1,0]
count=0
while True:
    count+=1
    n=int(input())
    if n==0:
        break
    data=list(list(map(int,input().split())) for _ in range(n))
    values=list([1e10 for _ in range(n)] for _ in range(n))
    values[0][0]=data[0][0]
    q=[]
    heapq.heappush(q,[values[0][0],0,0])
    while q:
        val,x,y=heapq.heappop(q)
        if x==n-1 and y==n-1:
            break
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n:
                if values[nx][ny]>values[x][y]+data[nx][ny]:
                    values[nx][ny]=values[x][y]+data[nx][ny]
                    heapq.heappush(q,[values[nx][ny],nx,ny])
    print("Problem ", count, ": ", values[n-1][n-1], sep="")