n=int(input())
dam=[0]+list(map(int,input().split()))
hap=[0]+list(map(int,input().split()))
dp=list(list(0 for _ in range(101)) for _ in range(n+1))
for i in range(1,n+1):
    for j in range(1,100):
        if j>=dam[i]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-dam[i]]+hap[i])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][99])