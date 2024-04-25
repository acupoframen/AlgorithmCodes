from datetime import datetime,timedelta
date1=datetime.strptime(input(),'%Y %m %d')
date2=datetime.strptime(input(),'%Y %m %d')
datediff=(date2 - date1).days
t,n=map(int,input().split())
dp=list(list(datediff for _ in range(t+1)) for _ in range(n+1))
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    for j in range(t+1):
        dp[i][j]=dp[i-1][j]
        if j>=b:
            if a==1:
                dp[i][j]=min(dp[i][j],dp[i-1][j-b]-c)
            elif a==2:
                dp[i][j]=min(dp[i][j],dp[i-1][j-b]-c)
            else:
                dp[i][j]=min(dp[i][j],dp[i-1][j-b]-c*30)

print(abs(min(dp[n])))