from collections import deque
n,m=map(int,input().split())
data=list(list(input()) for _ in range(n))
startx,starty=0,0
buildingcount=0
for i in range(n):
    for j in range(m):
        if data[i][j]=="@":
            startx,starty=i,j
            data[i][j]=='.'
        if data[i][j]=='*' or data[i][j]=='#':
            buildingcount+=1
visited=list(list(0 for _ in range(m)) for _ in range(n))
q=deque()
q.append([startx,starty])
dx=[-1,0,0,1]
dy=[0,-1,1,0]
flag=0
visited[startx][starty]=1
brokenbuilding=0
while q:
    x,y=q.popleft()
    if flag==0:
        for k in range(4):
            nx=x
            ny=y
            for _ in range(2):
                nx=nx+dx[k]
                ny=ny+dy[k]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if data[nx][ny]=='|':
                        visited[nx][ny]=1
                        break
                    elif data[nx][ny]=='*':
                        brokenbuilding+=1
                        data[nx][ny]='.'
                        visited[nx][ny]=1
                        q.append([nx,ny])
                    elif data[nx][ny]=='#':
                        data[nx][ny]='*'
        flag=1
    else:
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if data[nx][ny]=='|':
                    visited[nx][ny]=1
                    continue
                elif data[nx][ny]=='*':
                    brokenbuilding+=1
                    data[nx][ny]='.'
                    visited[nx][ny]=1
                    q.append([nx,ny])
                elif data[nx][ny]=='#':
                    data[nx][ny]='*'
print(brokenbuilding,buildingcount-brokenbuilding)