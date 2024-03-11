n,m=map(int,input().split())
data=list(list(map(int,input().split())))
#n is investment price, m is firms
dp=[[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        dp[i][j]=max(dp[i-1][j)
