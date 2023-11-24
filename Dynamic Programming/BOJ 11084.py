from collections import deque
n,m=map(int,input().split())
dist=[[-1 for _ in range(401)] for _ in range(401)]
dp=[[0 for _ in range(401)] for _ in range(401)]
dx=[[-1,-2],[-1,2],[1,-2],[1,2],[2,1],[2,-1],[-2,1],[-2,-1]]

q=deque([])
q.append([0,0])
dp[0][0]=1
while q:
    a,b=q.popleft()
    for i,j in dx:
        nx=a+i
        ny=b+j
        if 0<=nx<n and 0<=ny<m:
            if dist[nx][ny]==-1:
                dist[nx][ny]=dist[a][b]+1
                dp[nx][ny]=dp[a][b]
                q.append([nx,ny])
            elif dist[nx][ny]==dist[a][b]+1:
                dp[nx][ny]+=dp[a][b]
                dp[nx][ny]%=1000000009
if n==1 and m==1:
    print(0,1)
    exit(0)
if dist[n-1][m-1]==-1:
    print("None")
else:
    print(1+dist[n-1][m-1], dp[n-1][m-1])