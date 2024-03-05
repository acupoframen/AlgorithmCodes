n,m,k=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
from collections import deque
dice=[0,2,4,1,3,5,6]
d=0
x,y=0,0
answer=0
def roll(d):
    if d==0: #east
        dice[4],dice[3],dice[2],dice[6]=dice[3],dice[2],dice[6],dice[4]
    elif d==1: #south
        dice[1],dice[3],dice[5],dice[6]=dice[6],dice[1],dice[3],dice[5]
    elif d==2: #west
        dice[4],dice[3],dice[2], dice[6]=dice[6],dice[4],dice[3],dice[2]
    else: #north
        dice[1],dice[3],dice[5],dice[6] = dice[3],dice[5],dice[6],dice[1]

def play():
    global d,answer,x,y
    nx,ny=x,y
    if d==0:
        nx,ny=x,y+1
        if 0<=nx<n and 0<=ny<m:
            roll(d)
            answer+=data[nx][ny]*score(nx,ny)
        else:
            d=2
            play()
            return
    elif d==1:
        nx,ny=x+1,y
        if 0<=nx<n and 0<=ny<m:
            roll(d)
            answer+=data[nx][ny]*score(nx,ny)
        else:
            d=3
            play()
            return
    elif d==2:
        nx,ny=x,y-1
        if 0<=nx<n and 0<=ny<m:
            roll(d)
            answer+=data[nx][ny]*score(nx,ny)
        else:
            d=0
            play()
            return
    else:
        nx,ny=x-1,y
        if 0<=nx<n and 0<=ny<m:
            roll(d)
            answer+=data[nx][ny]*score(nx,ny)
        else:
            d=1
            play()
            return
    
    if dice[6]>data[nx][ny]:
        d+=1
        if d==4:
            d=0

    elif dice[6]<data[nx][ny]:
        d-=1
        if d==-1:
            d=3
    x,y=nx,ny
    return

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def score(xx,yy):
    count=1
    visited=list(list(0 for _ in range(m)) for _ in range(n))
    q=deque()
    q.append([xx,yy])
    visited[xx][yy]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and data[nx][ny]==data[xx][yy]:
                q.append([nx,ny])
                count+=1
                visited[nx][ny]=1
    return count

for _ in range(k):
    play()

print(answer)