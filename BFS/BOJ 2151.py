from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n=int(input())
data=list()
for _ in range(n):
    data.append(list(input()))
startx,starty=1e10,1e10
endx,endy=1e10,1e10
for i in range(n):
    for j in range(n):
        if data[i][j]=="#":
            if startx==1e10 and starty==1e10:
                startx=i
                starty=j
            else:
                endx=i
                endy=j

answer=[[[-1]*4 for _ in range(n)] for _ in range(n)]
q=deque()
for i in range(4):
    q.append([startx,starty,i])
    answer[startx][starty][i]=0
while q:
    x,y,d=q.popleft()
    if x==endx and y==endy:
        print(answer[x][y][d])
        break
    nx,ny=x+dx[d],y+dy[d]
    if 0<=nx<n and 0<=ny<n:
        if data[nx][ny]!="*":
            if answer[nx][ny][d]==-1 or answer[nx][ny][d]>answer[x][y][d]:
                answer[nx][ny][d]=answer[x][y][d]
                q.appendleft([nx,ny,d])
            if data[nx][ny]=="!":
                if d<2:
                    for i in range(2,4):
                        if answer[nx][ny][i]==-1 or answer[nx][ny][i]>answer[x][y][d]+1:
                            answer[nx][ny][i]=answer[x][y][d]+1
                            q.append([nx,ny,i])
                else:
                    for i in range(2):
                        if answer[nx][ny][i]==-1 or answer[nx][ny][i]>answer[x][y][d]+1:
                            answer[nx][ny][i]=answer[x][y][d]+1
                            q.append([nx,ny,i])
                        