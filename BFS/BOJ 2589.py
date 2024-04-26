a,b=map(int,input().split())
data=list(list(input()) for _ in range(a))
maxlen=a+b-2
answer=0

from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for i in range(a):
    for j in range(b):
        visited=list(list(-1 for _ in range(b)) for _ in range(a))
        if data[i][j]=='W':
            continue
        q=deque()
        q.append([i,j])
        visited[i][j]=0
        temp=0
        while q:
            x,y=q.popleft()
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<a and 0<=ny<b and visited[nx][ny]==-1 and data[nx][ny]=='L':
                    visited[nx][ny]=visited[x][y]+1
                    temp=max(temp,visited[nx][ny])
                    q.append([nx,ny])
        
        answer=max(answer,temp)


print(answer)