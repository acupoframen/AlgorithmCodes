n=int(input())
dp=[0,1]
for i in range(2,n+1):
    val=1e10
    for j in range(1,int(i**0.5)+1):
        val=min(val,dp[i-j**2])
    dp.append(val+1)
print(dp[n])