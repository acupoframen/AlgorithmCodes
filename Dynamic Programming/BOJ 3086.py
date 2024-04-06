dp=list(list(1e10 for _ in range(1001)) for _ in range(1001))
n,m=map(int,input().split())
n,m=min(m,n),max(m,n)

for i in range(1,m+1):
    dp[i][1]=i
    dp[1][i]=i

for i in range(2,n+1):
    dp[i][i]=1
    for k in range(1,i//2+1):
        for j in range(i+1,m+1):
            dp[i][j]=min(dp[i][j],dp[i-k][j]+dp[k][j])
    for j in range(i+1,m+1):
        for k in range(1,j//2+1):
            dp[i][j]=min(dp[i][j],dp[i][j-k]+dp[i][k])
    for j in range(i+1,m+1):
        dp[j][i]=dp[i][j]

print(dp[n][m])