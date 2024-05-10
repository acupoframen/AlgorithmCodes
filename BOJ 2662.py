n,m=map(int,input().split())
data=[[0 for _ in range(m+1)]]+list(list(map(int,input().split())) for _ in range(n))
dp=list(list(0 for _ in range(m+1)) for _ in range(n+1))
table=list(list(list(0 for _ in range(m+1)) for _ in range(m+1)) for _ in range(n+1))
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=max(dp[i][j-1],data[i][j])
        if dp[i][j]==data[i][j]:
            table[i][j][j]=i
        else:
            table[i][j]=table[i][j-1].copy()
        for k in range(1,i+1):
            if dp[i][j]<dp[k][j-1]+data[i-k][j]:
                dp[i][j]=dp[k][j-1]+data[i-k][j]
                table[i][j]=table[k][j-1].copy()
                table[i][j][j]=i-k

print(dp[-1][-1])
print(*table[-1][-1][1:])