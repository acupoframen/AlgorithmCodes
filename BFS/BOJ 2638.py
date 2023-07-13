from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))


time=0
dx=[[0,1],[0,-1],[1,0],[-1,0]]
while True:
    q=deque([[0,0]])
    cheeseMelt=False
    while q:
        x,y=q.popleft()
        for a,b in dx:
            nx=a+x
            ny=b+y
            if 0<=nx<n and 0<=ny<m and data[nx][ny]!=-1: 
                if data[nx][ny]>=1:
                    data[nx][ny]+=1
                if data[nx][ny]==0:
                    data[nx][ny]=-1
                    q.append([nx,ny])
    for i in range(n):
        for j in range(m):
            if data[i][j]>2:
                data[i][j]=0
                cheeseMelt=True
            if data[i][j]==2:
                data[i][j]=1
                cheeseMelt=True
            if data[i][j]==-1:
                data[i][j]=0
    time+=1
    if not cheeseMelt:
        print(time-1)
        break
