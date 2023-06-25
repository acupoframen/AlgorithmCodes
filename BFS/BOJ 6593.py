import sys
input=sys.stdin.readline
from collections import deque
dx=[1,-1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]
def bfs(q):
    while q:
        i,j,k=q.popleft()
        for d in range(6):
            nx=dx[d]+i
            ny=dy[d]+j
            nz=dz[d]+k
            if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                if data[nx][ny][nz]=='E':
                    return data[i][j][k]+1
                if data[nx][ny][nz]=='.':
                    data[nx][ny][nz]=(data[i][j][k]+1)
                    q.append([nx,ny,nz])
    return 1e10
while True:
    l,r,c=map(int,input().split())
    start=[]
    end=[]
    if l==0:
        break
    data=[]
    for _ in range(l):
        temp=[]
        for _ in range(r):
            temp.append(list(input().strip()))
        data.append(temp)
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if data[i][j][k]=='S':
                    start=[i,j,k]
                    data[i][j][k]=0
    q=[start]
    q=deque(q)
    answer=bfs(q)
    if answer==1e10:
        print("Trapped!")
    else:
        print("Escaped in "+str(answer)+" minute(s).")