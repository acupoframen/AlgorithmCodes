n=int(input())
dp=[[0 for _ in range(10)] for _ in range(n+1)]
dp[0]=[0,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    for j in range(1,10):
        if j==1:
            dp[i][1]=sum(dp[i-1][1:4])%987654321
        elif j==2:
            dp[i][2]=sum(dp[i-1][1:5])%987654321
        elif j==8:
            dp[i][8]=sum(dp[i-1][6:10])%987654321
        elif j==9:
            dp[i][9]=sum(dp[i-1][7:10])%987654321
        else:
            dp[i][j]=sum(dp[i-1][j-2:j+3])%987654321

print(sum(dp[n-1])%987654321)