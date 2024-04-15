n,m=map(int,input().split())
data=list([1e10]+list(map(int,input().split()))+[1e10] for _ in range(n))
dp=list(list(list(1e10 for _ in range(m+2)) for _ in range(n)) for _ in range(3))
for i in range(3):
    dp[i][0]=data[0]
for j in range(1,n):
    for i in range(1,m+1):
        for k in range(3):
            if k==0:
                dp[k][j][i]=min(dp[1][j-1][i],dp[2][j-1][i-1])
            elif k==1:
                dp[k][j][i]=min(dp[0][j-1][i+1],dp[2][j-1][i-1])
            else:
                dp[k][j][i]=min(dp[0][j-1][i+1],dp[1][j-1][i])
            dp[k][j][i]+=data[j][i]
answer=1e10
for i in range(1,m+1):
    for k in range(3):
        answer=min(answer,min(dp[k][n-1]))

print(answer)