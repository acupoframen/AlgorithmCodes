from collections import deque
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
landnum=2
dx=[-1,0,0,1]
dy=[0,1,-1,0]
lands=[]
for i in range(n):
    for j in range(n):
        if data[i][j]>=2:
            continue
        elif data[i][j]==0:
            continue
        q=deque()
        q.append([i,j])
        temp=[]
        data[i][j]=landnum
        temp.append([i,j])
        while q:
            x,y=q.popleft()
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<n and 0<=ny<n and data[nx][ny]==1:
                    q.append([nx,ny])
                    temp.append([nx,ny])
                    data[nx][ny]=landnum
        lands.append(temp)
        landnum+=1
answer=1e10
landnum=1
for land in lands:
    landnum+=1
    for x,y in land:
        q=deque()
        q.append([x,y,0])
        visited=[[0 for _ in range(n)] for _ in range(n)]
        visited[x][y]=1
        while q:
            xx,yy,val=q.popleft()
            if data[xx][yy]>=2 and data[xx][yy]!=landnum:
                answer=min(answer,val)
                break
            for k in range(4):
                nx=xx+dx[k]
                ny=yy+dy[k]
                if 0<=nx<n and 0<=ny<n and data[nx][ny]!=landnum and visited[nx][ny]==0:
                    q.append([nx,ny,val+1])
                    visited[nx][ny]=1

print(answer-1)