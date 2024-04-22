from collections import deque

n,m,k=map(int,input().split())
data=list(list(1e10 for _ in range(m)) for _ in range(n))
for _ in range(k):
    a,b=map(int,input().split())
    data[a][b]=-1


data[0][0]=0
q=deque()
q.append([0,0])
dx1=[0,0,-1,-1,1,1]
dy1=[1,-1,-1,0,0,-1]
dx2=[0,0,-1,-1,1,1]
dy2=[-1,1,0,1,0,1]
while q:
    x,y=q.popleft()
    if x==n-1 and y==m-1:
        print(data[x][y])
        exit(0)
    for k in range(6):
        if x%2:
            nx=x+dx2[k]
            ny=y+dy2[k]
            if 0<=nx<n and 0<=ny<m and data[nx][ny]>data[x][y]+1 and data[nx][ny]!=-1:
                data[nx][ny]=data[x][y]+1
                q.append([nx,ny])
        else:
            nx=x+dx1[k]
            ny=y+dy1[k]
            if 0<=nx<n and 0<=ny<m and data[nx][ny]>data[x][y]+1 and data[nx][ny]!=-1:
                data[nx][ny]=data[x][y]+1
                q.append([nx,ny])

print(-1)