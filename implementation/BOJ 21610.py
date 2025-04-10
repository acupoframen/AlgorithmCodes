import sys
from copy import deepcopy
input=sys.stdin.readline
n,m=map(int,input().split())
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
data=list(list(map(int,input().split())) for _ in range(n))
cloud=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
def movecloud(d,s):
    global cloud
    newcloud=[]
    for x,y in cloud:
        nx=(x+dx[d]*s)%n
        ny=(y+dy[d]*s)%n
        newcloud.append((nx,ny))
    cloud=newcloud[:]
def rain():
    global cloud
    before=deepcopy(cloud)
    visited=list(list(0 for _ in range(n)) for _ in range(n))
    for x,y in cloud:
        data[x][y]+=1
        visited[x][y]=1
    cloud=[]
    return before,visited

ddx=[-1,1,-1,1]
ddy=[-1,1,1,-1]
def func(before,visited):
    for x,y in before:
        count=0
        for i in range(4):
            nx=x+ddx[i]
            ny=y+ddy[i]
            if 0<=nx<n and 0<=ny<n and data[nx][ny]>0:
                count+=1
        data[x][y]+=count
    for i in range(n):
        for j in range(n):
            if data[i][j]>=2:
                if not visited[i][j] and data[i][j]>=2:
                    data[i][j]-=2
                    cloud.append((i,j))
for i in range(m):
    d,s=map(int,input().split())
    movecloud(d-1,s)
    before,visited=rain()
    func(before,visited)

water=0
for i in range(n):
    for j in range(n):
        water+=data[i][j]

print(water)