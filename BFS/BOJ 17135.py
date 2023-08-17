import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque
from copy import deepcopy
n,m,d=map(int,input().split())
data=[list(map(int,input().strip().split())) for _ in range(n)]

possible=combinations([i for i in range(0,m)],3)

dx=[-1,0,0]
dy=[0,-1,1]
answer=0
for i in possible:
    tempdata=deepcopy(data)
    tempanswer=0
    for j in range(n):
        shot=list()
        for k in i:
            q=deque()
            q.append([n-j-1,k,1])
            visited=[[0 for _ in range(m)] for _ in range(n)]
            visited[n-j-1][k]=1
            distance=1e10
            temp=[1e10,1e10]
            while q:
                a,b,c=q.popleft()
                visited[a][b]=1
                if c>distance or c>d:
                    break
                if tempdata[a][b]==1:
                    if distance>c:
                        distance=c
                        temp=[a,b]
                    elif distance==c:
                        if b<temp[1]:
                            temp=[a,b]
                else:
                    for i2 in range(3):
                        nx=dx[i2]+a
                        ny=dy[i2]+b
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                            q.append([nx,ny,c+1])
            shot.append(temp)
        for i1 in shot:
            if i1[0]==1e10 or i1[1]==1e10:
                continue
            if tempdata[i1[0]][i1[1]]:
                tempanswer+=1
                tempdata[i1[0]][i1[1]]=0
    if tempanswer>answer:
        
        answer=tempanswer
print(answer)
