n=int(input())
left=[0]+[int(input()) for _ in range(n)]
right=[0]+[int(input()) for _ in range(n)]
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        if abs(left[i]-right[j])<=4:
            dp[i][j]=dp[i-1][j-1]+1
print(dp[n][n])