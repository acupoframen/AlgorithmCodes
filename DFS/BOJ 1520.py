n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
dx=[0,0,-1,1]
dy=[1,-1,0,0]
dp=list(list(-1 for _ in range(m)) for _ in range(n))

def dfs(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    count=0
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny]>=data[x][y]:
                continue
            count+=dfs(nx,ny)
    dp[x][y]=count

    return dp[x][y]

dp[n-1][m-1]=1
print(dfs(0,0))