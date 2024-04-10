n=int(input())
dp=list(0 for _ in range(1616))
for i in range(2,n+1):
    if i%2:
        dp[i]=2*dp[i-1]-1
    else:
        dp[i]=2*dp[i-1]+1
    dp[i]%=1000000007
print(dp[n])
