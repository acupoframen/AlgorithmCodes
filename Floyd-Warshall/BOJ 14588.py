n=int(input())
dp=list(list(1e10 for _ in range(n+1)) for _ in range(n+1))
data=[1e10]
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][1]<data[j][0] or data[j][1]<data[i][0]:
            continue
        dp[i][j]=1
        dp[j][i]=1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==k or i==j or j==k:
                continue
            dp[i][j]=min(dp[i][j],dp[k][i]+dp[k][j])
            dp[j][i]=min(dp[i][j],dp[k][i]+dp[k][j])
q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    if dp[a][b]==1e10:
        print(-1)
    else:
        print(dp[a][b])