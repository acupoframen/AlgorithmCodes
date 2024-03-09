from collections import deque

r,c=map(int,input().split())
data=list(list(input()) for _ in range(r))

answer=list(list(1e10 for _ in range(c)) for _ in range(r))
waters=[]
q=deque()
for i in range(r):
    for j in range(c):
        if data[i][j]=='S':
            q.append([i,j])
            answer[i][j]=0
        elif data[i][j]=='*':
            waters.append([i,j])
            

dx=[0,0,-1,1]
dy=[1,-1,0,0]

time=0
def water():
    global waters,time
    temp=[]
    while waters:
        x,y=waters.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and data[nx][ny]=='.':
                data[nx][ny]='*'
                temp.append([nx,ny])
    waters=temp
    time+=1

while q:
    x,y=q.popleft()
    if answer[x][y]==time:
        water()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and answer[nx][ny]==1e10:
            if data[nx][ny]=='D':
                print(answer[x][y]+1)
                exit(0)
            elif data[nx][ny]=='.':
                q.append([nx,ny])
                answer[nx][ny]=answer[x][y]+1


print("KAKTUS")