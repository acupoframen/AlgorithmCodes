import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=[0]+list(int(input()) for _ in range(n))
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j-1]+data[i]
    for j in range(1,m+1):
        if i<j:
            break
        dp[i][0]=max(dp[i][0],dp[i-j][j],dp[i-j][0])

print(dp[n][0])