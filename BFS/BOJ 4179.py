from collections import deque
r,c=map(int,input().split())
data=list(list(input()) for _ in range(r))
time=0
fire=deque()
jihoon=deque()

visited=list(list(0 for _ in range(c)) for _ in range(r))
for i in range(r):
    for j in range(c):
        if data[i][j]=='F':
            fire.append([i,j,0])
        elif data[i][j]=='J':
            jihoon.append([i,j,0])
            data[i][j]='.'
            visited[i][j]=1
dx=[0,0,-1,1]
dy=[1,-1,0,0]
while jihoon:
    
    x,y,val=jihoon.popleft()
    
    if fire and fire[0][2]==val-1:
        while True:
            firex,firey,firec=fire.popleft()
            if firec==val:
                fire.appendleft([firex,firey,firec])
                break
            for k in range(4):
                nx=firex+dx[k]
                ny=firey+dy[k]
                if 0<=nx<r and 0<=ny<c and data[nx][ny]=='.':
                    data[nx][ny]='F'
                    fire.append([nx,ny,firec+1])
    if data[x][y]=='F':
        continue
    if x in [0, r-1] or y in [0, c-1]:
        print(val+1)
        exit(0)
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<r and 0<=ny<c and data[nx][ny]=="." and not visited[nx][ny]:
            jihoon.append([nx,ny,val+1])
            visited[nx][ny]=1

print("IMPOSSIBLE")