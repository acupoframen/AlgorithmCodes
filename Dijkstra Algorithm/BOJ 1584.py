import heapq
data=[[0 for _ in range(501)] for _ in range(501)]
minpoint=[[1e10 for _ in range(501)] for _ in range(501)]
n=int(input())
for _ in range(n):
    a,b,c,d=map(int,input().split())
    x1=min(a,c)
    x2=max(a,c)
    y1=min(b,d)
    y2=max(b,d)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            data[i][j]=-1
n=int(input())
for _ in range(n):
    a,b,c,d=map(int,input().split())
    x1=min(a,c)
    x2=max(a,c)
    y1=min(b,d)
    y2=max(b,d)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            data[i][j]=1e10

q=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
heapq.heappush(q,[0,0,0])
while q:
    point,x,y=heapq.heappop(q)    
    if point>minpoint[x][y]:
        continue
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<501 and 0<=ny<501:
            if data[nx][ny]==1e10:
                continue
            elif data[nx][ny]==-1:
                if point+1<minpoint[nx][ny]:
                    minpoint[nx][ny]=point+1
                    heapq.heappush(q,[point+1,nx,ny])
            else:
                if point<minpoint[nx][ny]:
                    minpoint[nx][ny]=point
                    heapq.heappush(q,[point,nx,ny])

if minpoint[500][500]==1e10:
    print(-1)
else:
    print(minpoint[500][500])