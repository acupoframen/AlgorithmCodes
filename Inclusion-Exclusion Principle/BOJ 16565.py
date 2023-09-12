import sys, math
n=int(input())
dp=[[0]*53 for _ in range(53)]

for i in range(53):
    dp[i][0]=1
for i in range(1,53):
    for j in range(1,53):
        dp[i][j]=(dp[i-1][j]+dp[i-1][j-1])%10007
answer=0
for i in range(1,14):
    if n-4*i<0:
        break
    if i%2==1:
        answer=(answer+dp[52-4*i][n-4*i]*dp[13][i])%10007
    else:
        answer=answer-(dp[52-4*i][n-4*i]*dp[13][i]%10007+10007)%10007

print(answer%10007)