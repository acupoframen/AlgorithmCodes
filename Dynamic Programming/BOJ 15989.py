t=int(input())
for _ in range(t):
    n=int(input())
    dp=[[1e10,0,0,0] for _ in range(10001)]
    dp[1][1]=1
    dp[2][1]=1
    dp[2][2]=1
    dp[3][1]=2
    dp[3][3]=1
    if n<=3:
        print(sum(dp[n][1:]))
        continue
    for i in range(4,n+1):
        for j in range(1,4):
            if j==1:
                dp[i][1]=dp[i-1][1]+dp[i-1][2]+dp[i-1][3]
            elif j==2:
                dp[i][2]=dp[i-2][3]+dp[i-2][2]
            else:
                dp[i][3]=dp[i-3][3]
    print(sum(dp[n][1:]))