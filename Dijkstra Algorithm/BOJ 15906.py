import sys
import heapq
input=sys.stdin.readline
dx=[[1,0],[0,1],[-1,0],[0,-1]]
n,t,r,c=map(int,input().split())
coords=[list(input()) for _ in range(n)]
r-=1;c-=1
data= [[[1e10,1e10] for _ in range(n)] for _ in range(n)]
data[0][0][0]=0
q=[]
heapq.heappush(q,[0,0,0,0])
while q:
    pastVal,y,x,mode=heapq.heappop(q)
    if mode==1 and data[y][x][0]>=pastVal: #변신 to 일반
        data[y][x][0]=pastVal
        heapq.heappush(q,[pastVal,y,x,0])
    if mode==0:
        for a,b in dx : #일반 to 일반
            ny,nx=y+a,x+b
            if 0<=ny<n and 0<=nx<n and data[ny][nx][0]>pastVal+1:
                data[ny][nx][0]=data[y][x][0]+1
                heapq.heappush(q,[pastVal+1,ny,nx,0])
    if mode==0 and data[y][x][1]>pastVal+t: #일반 to 변신
        data[y][x][1]=pastVal+t
        heapq.heappush(q,[pastVal+t,y,x,1])
    if mode==1: #변신 to 변신
        for i in range(4):
            ny,nx=y+dx[i][0],x+dx[i][1]
            found=0
            while 0<=nx<n and 0<=ny<n:
                if coords[ny][nx]=="#":
                    found=1
                    break
                ny,nx=ny+dx[i][0],nx+dx[i][1]
            if found and data[ny][nx][1]>pastVal+1:
                data[ny][nx][1]=pastVal+1
                heapq.heappush(q,[pastVal+1,ny,nx,1])
print(data)
print(min(data[r][c]))

