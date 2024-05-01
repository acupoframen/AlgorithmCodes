from copy import deepcopy
r,c=map(int,input().split())
data=list(list(input()) for _ in range(r))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
newdata=deepcopy(data)
for i in range(r):
    for j in range(c):
        if data[i][j]=='X':
            temp=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<r and 0<=ny<c:
                    if data[nx][ny]=='.':
                        temp+=1
                else:
                    temp+=1
            if temp>=3:
                newdata[i][j]='.'

north=r
east=-1
south=-1
west=c
for i in range(r):
    for j in range(c):
        if newdata[i][j]=='X':
            north=min(i,north)
            east=max(j,east)
            south=max(i,south)
            west=min(j,west)
for i in range(north,south+1):
    print(*newdata[i][west:east+1] ,sep="")