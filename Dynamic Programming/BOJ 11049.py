n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
dp=list(list(0 for _ in range(n)) for _ in range(n))

for i in range(1,n):
    for j in range(0,n-i):
        if i==1:
            dp[j][j+1]= data[j][0]*data[j][1]*data[j+1][i]
        temp=1e12
        for k in range(j,j+i):
            temp=min(temp,dp[j][k]+dp[k+1][j+i]+data[j][0]*data[k][1]*data[j+i][1])
        dp[j][j+i]=temp
print(dp[0][n-1])