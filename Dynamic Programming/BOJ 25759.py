n=int(input())
data=[0]+list(map(int,input().split()))
dp=[-1e10 for _ in range(101)]
dp[data[1]]=0
for i in range(2,n+1):
    for j in range(1,101):
        if dp[j]!=-1e10:
            dp[data[i]]=max(dp[data[i]],dp[j]+(data[i]-j)**2)
print(max(dp))