n,t=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
answer=sum(m for _,m in data)
dp=list(list(0 for _ in range(t+1)) for _ in range(n+1))

for i in range(1,n+1):
    d,m=data[i-1]
    for j in range(t+1):
        dp[i][j]=dp[i-1][j]
        if j>=d:
            dp[i][j]=max(dp[i][j],dp[i-1][j-d]+m)
print(answer-dp[n][t])