n=int(input())
data=list([0])
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
dp=[0 for _ in range(n+2)]
for i in range(1,n+1):
    time,price=data[i]
    dp[i]=max(dp[i],dp[i-1])
    if time+i<=n+1:
        dp[time+i-1]=max(dp[time+i-1],dp[i-1]+price)
print(max(dp))