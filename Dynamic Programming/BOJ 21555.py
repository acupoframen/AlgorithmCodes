n,k=map(int,input().split())
dp=[[0,0] for _ in range(n+1)]
a=[0]+list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    dp[i][0]=min(dp[i-1][0]+a[i],dp[i-1][1]+a[i]+k)
    dp[i][1]=min(dp[i-1][1]+b[i],dp[i-1][0]+b[i]+k)
print(min(dp[-1]))
print(dp)