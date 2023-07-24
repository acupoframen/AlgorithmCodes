import sys
input=sys.stdin.readline
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
dp=[[[0 for _ in range(3)] for _ in range(n)]for _ in range(n)]
for i in range(1,n):
    if data[0][i]==0:
        dp[0][i][0]=1
    else:
        break
for i in range(1,n):
    for j in range(1,n):
        if data[i][j]==1:
            continue
        if not  data[i-1][j-1] and not data[i-1][j] and not data[i][j-1]:
            dp[i][j][1]=sum(dp[i-1][j-1])
        if not data[i-1][j]:
            dp[i][j][2]=dp[i-1][j][1]+dp[i-1][j][2]
        if not data[i][j-1]:
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][1]
print(sum(dp[n-1][n-1]))