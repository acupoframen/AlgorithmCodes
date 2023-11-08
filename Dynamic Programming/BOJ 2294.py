n,k=map(int,input().split())
coin=list(int(input()) for _ in range(n))
coin.sort()
dp=[1e10 for _ in range(k+1)]
dp[0]=0
for i in coin:
    for j in range(i,k+1):
        dp[j]=min(dp[j-i]+1,dp[j])

if dp[-1]==1e10:
    print(-1)
else:
    print(dp[-1])