from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[1,-1,0,0]
r,c=map(int,input().split())
data=list(list(input().strip()) for _ in range(r))
visited=[[0 for _ in range(c)] for _ in range(r)]
swanvisited=[[0 for _ in range(c)] for _ in range(r)]
newswan=deque()
oldswan=deque()
newwater=deque()
oldwater=deque()
swan=[]
for i in range(r):
    for j in range(c):
        if data[i][j]=="L":
            oldwater.append([i,j])
            if not swan:
                oldswan.append([i,j])
            swan.append([i,j])
            
            data[i][j]='.'
        elif data[i][j]==".":
            oldwater.append([i,j])
            visited[i][j]=1
time=0
while True:
    while oldwater:
        a,b=oldwater.popleft()
        data[a][b]='.'
        for i in range(4):
            nx,ny=a+dx[i],b+dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if data[nx][ny]=='.':
                    oldwater.append([nx,ny])
                else:
                    newwater.append([nx,ny])
                visited[nx][ny]=1
    while oldswan:
        a,b=oldswan.popleft()
        if [a,b]==swan[1]:
            print(time)
            exit(0)
        for i in range(4):
            for i in range(4):
                nx,ny=a+dx[i],b+dy[i]
                if 0<=nx<r and 0<=ny<c and not swanvisited[nx][ny]:
                    if data[nx][ny]=='.':
                        oldswan.append([nx,ny])
                    else:
                        newswan.append([nx,ny])
                    swanvisited[nx][ny]=1
    oldswan=newswan
    oldwater=newwater
    newswan=deque()
    newwater=deque()
    time+=1
