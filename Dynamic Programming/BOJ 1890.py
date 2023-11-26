n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if data[i][j]==0:
            continue
        if 0<=i+data[i][j]<n:
            dp[i+data[i][j]][j]+=dp[i][j]
        if 0<=j+data[i][j]<n:
            dp[i][j+data[i][j]]+=dp[i][j]

print(dp[-1][-1])