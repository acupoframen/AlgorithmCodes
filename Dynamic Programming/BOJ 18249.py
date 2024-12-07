import sys
input=sys.stdin.readline
t=int(input())
dp=list(0 for _ in range(191230))
dp[1]=1
dp[2]=2
mod=(int(1e9)+7)
for i in range(3,191230):
    dp[i]=(dp[i-2]+dp[i-1])%mod
for _ in range(t):
    n=int(input())
    print(dp[n])
