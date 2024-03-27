import sys
sys.setrecursionlimit(500**2)
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
dp=[[0 for _ in range(n)] for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y]=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n and data[x][y]<data[nx][ny]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]
for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs(i,j)

answer=0
for i in range(n):
    answer=max(answer,max(dp[i]))

print(answer)