from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(m))
dx=[1,0]
dy=[0,1]
q=deque()
q.append([0,0])
visited=list(list(0 for _ in range(n)) for _ in range(m))
visited[0][0]=1
while q:
    x,y=q.popleft()
    if x==m-1 and y==n-1:
        print("Yes")
        exit()
    for i in range(2):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<m and 0<=ny<n and data[nx][ny] and not visited[nx][ny]:
            q.append([nx,ny])
            visited[nx][ny]=1

print("No")