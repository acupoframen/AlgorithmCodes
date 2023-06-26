n,m,d=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
dp=[[-1e10 for _ in range(m)] for _ in range(n)]
for i in range(0,m):
    dp[0][i]=0
for i in range(0,n-1):
    for j in range(m):
        for k in range(1,d+1):
            for l in range(j-d+k,j+d-k+1):
                if i+k<n and 0<=l<m:
                    if data[i][j]*data[i+k][l]+dp[i][j]>dp[i+k][l]:
                        dp[i+k][l]=data[i][j]*data[i+k][l]+dp[i][j]
                if i+k>=n or l>=m:
                    break
answer=-1e10
for i in range(0,m):
    answer=max(answer,dp[n-1][i])
print(answer)