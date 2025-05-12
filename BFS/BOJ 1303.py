from collections import deque
n,m=map(int,input().split())
data=list(list(input()) for _ in range(m))
wcount=0
bcount=0
visited=list(list(0 for _ in range(n)) for _ in range(m))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            temp=0
            visited[i][j]=1
            q=deque()
            q.append((i,j))
            while q:
                x,y=q.popleft()
                if data[x][y]==data[i][j]:
                    temp+=1
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and data[nx][ny]==data[i][j]:
                            visited[nx][ny]=1
                            q.append((nx,ny))
            if data[i][j]=='W':
                wcount+=temp*temp
            else:
                bcount+=temp*temp
print(wcount,bcount)