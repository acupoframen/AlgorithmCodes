n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=1e10
for k in range(3):
    dp=list([1e10 for _ in range(3)] for _ in range(n))
    dp[0][k]=data[0][k]
    for i in range(1,n):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+data[i][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+data[i][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+data[i][2]
    for j in range(3):
        if k!=j:
            answer=min(answer,dp[-1][j])
print(answer)