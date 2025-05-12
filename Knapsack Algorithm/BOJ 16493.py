n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(m))
data.sort(key=lambda x: x[0])
dp=list(list(0 for _ in range(n+1)) for _ in range(m+1))
for i in range(m):
    for j in range(n+1):
        if j>=data[i][0]:
            dp[i+1][j]=max(dp[i][j],dp[i][j-data[i][0]]+data[i][1])
        else:
            dp[i+1][j]=dp[i][j]
print(dp[m][n])
