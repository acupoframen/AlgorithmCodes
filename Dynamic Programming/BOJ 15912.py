n=int(input())
w=list(map(int,input().split()))
e=list(map(int,input().split()))
dp=[1e10]*(n+1)
dp[0]=w[0]*e[0]
for i in range(1,n):
    dp[i]=max(e[:i+1])*max(w[:i+1])
    for j in range(1,i+1):
        dp[i]=min(dp[j-1]+max(w[j:i+1])*max(e[j:i+1]), dp[i])
print(dp[n-1])