from collections import deque
n,m=map(int,input().split())
data=list(list(0 for _ in range(n+1)) for _ in range(2*n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[a][b]=1e10

q=deque()
q.append([0,0])
while q:
    x,y=q.popleft()
    if x==2*n and y==0:
        print(data[2*n][0])
        exit(0)
    if 0<=y+1<=n and x+y+2<=2*n and data[x+1][y+1]!=1e10:
        if data[x+1][y+1]==0:
            q.append([x+1,y+1])
        if data[x+1][y+1]<=max(y+1,data[x][y]):
            data[x+1][y+1]=max(y+1,data[x][y])
    if 0<=y-1<=n and x+y<=2*n and data[x+1][y-1]!=1e10:
        if data[x+1][y-1]==0:            
            q.append([x+1,y-1])
        if data[x+1][y-1]<=data[x][y]:
            data[x+1][y-1]=data[x][y]
print(-1)