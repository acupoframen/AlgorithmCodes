import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
visited=list(list(0 for _ in range(m)) for _ in range(n))
land=[]

def name (i,j,num):
    q=deque()
    q.append([i,j])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny] and not visited[nx][ny]:
                    data[nx][ny]=num
                    land.append([nx,ny,num])
                    visited[nx][ny]=1
                    q.append([nx,ny])

def number():
    num=1
    for i in range(n):
        for j in range(m):
            if data[i][j] and not visited[i][j]:
                visited[i][j]=1
                data[i][j]=num
                name(i,j,num)
                land.append([i,j,num])
                num+=1
    return num-1

bridges=[]

def bridgemake(xx,yy,c):
    for i in range(4):
        q=deque()
        q.append([xx,yy])
        bridgedata=[[0 for _ in range(m)] for _ in range(n)]
        while q:
            x,y=q.popleft()
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny]==0:
                    bridgedata[nx][ny]=bridgedata[x][y]+1
                    q.append([nx,ny])
                elif data[nx][ny]!=c and bridgedata[x][y]>=2:

                    bridges.append([bridgedata[x][y],c,data[nx][ny]])
                    break
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

num=number()

for x,y,c in land:
    bridgemake(x,y,c)

parent=[i for i in range(num+1)]
answer,count=0,0
bridges.sort()
for d,a,b in bridges:
    if find(a) != find (b):
        union(a,b)
        answer+=d
        count+=1
        if count==num-1:
            break

if count==num-1:
    print(answer)
else:
    print(-1)