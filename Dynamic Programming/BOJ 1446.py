n,d=map(int,input().split())
dp=list(i for i in range(d+1))
dp[0]=0
data=list(list(map(int,input().split())) for _ in range(n))
data.sort()
for j in range(n):
    start,end,leng=data[j]
    if end>d:
        continue
    if end-start<leng:
        continue
    dp[end]=min(dp[end],dp[start]+leng)
    for i in range(1,d+1):
        dp[i]=min(dp[i-1]+1,dp[i])
print(dp[d])
