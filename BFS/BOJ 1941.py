from itertools import combinations
from collections import deque

data=list(list(input()) for _ in range(5))
coord=[[i,j] for i in range(5) for j in range(5)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=0

for i in combinations(coord,7):
    xcount=0
    ycount=0
    visited=[[0 for _ in range(5)] for _ in range(5)]
    count=1
    for x,y in i:
        if data[x][y]=='S':
            xcount+=1
        elif data[x][y]=='Y':
            ycount+=1
    if xcount<4:
        continue
    q=deque()
    q.append([i[0][0],i[0][1]])
    visited[i[0][0]][i[0][1]]=1

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                visited[nx][ny]=1
                if [nx,ny] in i:
                    q.append([nx,ny])
                    count+=1
    if count==7:
        answer+=1

print(answer)