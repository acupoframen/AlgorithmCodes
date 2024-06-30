from collections import deque
w,h=map(int,input().split())
data=list(list(input()) for _ in range(h))
c=[]
for i in range(h):
    for j in range(w):
        if data[i][j]=='C':
            c.append([i,j])
dx=[0,0,-1,1]
dy=[1,-1,0,0]
minturns=list(list(list(1e10 for _ in range(4)) for _ in range(w)) for _ in range(h))
q=deque()
for i in range(4):
    minturns[c[0][0]][c[0][1]][i]=0
for i in range(4):
    nx=c[0][0]+dx[i]
    ny=c[0][1]+dy[i]
    if 0<=nx<h and 0<=ny<w and data[nx][ny]==".":
        q.append([nx,ny,0,i])
        minturns[nx][ny][i]=0
#x,y,turns,direction
while q:
    x,y,turns,currdir=q.popleft()
    if x==c[1][0] and y==c[1][1]:
        minturns[x][y][i]=min(minturns[x][y][i],turns)
        continue
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and data[nx][ny] in ('.','C'):
            if i==currdir and minturns[nx][ny][i]>turns:
                q.append([nx,ny,turns,i])
                minturns[nx][ny][i]=turns
            elif i+currdir not in [1,5] and minturns[nx][ny][i]>turns+1:
                q.append([nx,ny,turns+1,i])
                minturns[nx][ny][i]=turns+1

print(min(minturns[c[1][0]][c[1][1]]))