n=int(input())
dp=[1e10 for _ in range(n+1)]

if n==1:
    print(-1)
    exit(0)
dp[2]=1
for i in range(2,n+1):
    dp[i]=min(dp[i-2]+1,dp[i])
    if i>=5:    
        dp[5]=1
        dp[i]=min(dp[i],dp[i-5]+1)
if dp[n]==1e10:
    print(-1)
else:
    print(dp[n])
