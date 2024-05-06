n=int(input())
data=[0]+list(map(int,list(input())))
dp=[0 for _ in range(n+1)]
dp[1]=1
for i in range(2,n+1):
    if i>=3 and data[i-2]!=0 and int("".join(map(str,data[i-2:i+1])))<=641:
        dp[i]=min(dp[i-1],dp[i-2],dp[i-3])+1
    elif data[i-1]!=0:
        dp[i]=min(dp[i-1],dp[i-2])+1
    else:
        dp[i]=dp[i-1]+1
print(dp[n])