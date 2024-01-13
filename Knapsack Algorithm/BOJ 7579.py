n,m=map(int,input().split())
data=list(map(int,input().split()))
cost=list(map(int,input().split()))
answer=1e10
total=sum(cost)
dp=[[0 for _ in range(total+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(total):
        if cost[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],data[i]+dp[i-1][j-cost[i]])
        if dp[i][j]>=m:
            answer=min(answer,j)
if sum(cost)==0:
    print(0)
    exit(0)
if answer==1e10:
    print(total)
else:
    print(answer)