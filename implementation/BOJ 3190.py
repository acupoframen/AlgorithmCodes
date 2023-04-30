from collections import deque
n=int(input())
data=[[0 for _ in range(n+1)] for _ in range(n+1)]
k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    data[a][b]=1
l=int(input())
movements=[]
for _ in range(l):
    a,b=input().split()
    movements.append([int(a),b])
dx=[[0,1],[1,0],[0,-1],[-1,0]]
snake=deque()
x,y=1,1
turn=0
time=0
i=0
snake.append([x,y])
movements.append([100001,100001])
while l:
    x+=dx[turn][0]
    y+=dx[turn][1]
    time+=1
    if x<1 or x>n or y<1 or y>n or [x,y] in snake:
        break
    snake.append([x,y])
    if data[x][y]==0:
        snake.popleft()
    else:
        data[x][y]=0
    if time==movements[i][0]:
        if movements[i][1]=='L':
            turn-=1
            i+=1
        else:
            turn+=1
            i+=1
        if turn==4:
            turn=0
        if turn==-1:
            turn=3
print(time)