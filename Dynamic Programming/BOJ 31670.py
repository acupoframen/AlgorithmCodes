n=int(input())
data=[1e10]+list(map(int,input().split()))
dp=[[0,0] for _ in range(n+1)]
dp[1]=[0,data[1]]
for i in range(2,n+1):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=min(dp[i-1])+data[i]

print(min(dp[n]))