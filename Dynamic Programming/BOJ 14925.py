m,n=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(m))
dp=list(list(0 for _ in range(n+1)) for  _ in range(m+1))
for i in range(1,m+1):
    for j in range(1,n+1):
        if not data[i-1][j-1]:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

answer=0
for i in range(m+1):
    answer=max(answer,max(dp[i]))
print(answer)