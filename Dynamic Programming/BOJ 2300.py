n=int(input())
coord=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    if coord[i][1]<0:
        coord[i][1]*=-1
coord.sort()
coord=[[-1e10,-1e10]]+coord[:]
dp=[0]*(n+1)
dp[0]=0
for i in range(1,n+1):
    dp[i]=dp[i-1]+coord[i][1]*2
    ymax=coord[i][1]*2
    for j in range(i-1,0,-1):
        ymax=max(coord[j][1]*2,ymax)
        maxlen=max(coord[i][0]-coord[j][0],ymax)
        dp[i]=min(dp[i],dp[j-1]+maxlen)
print(dp[n])