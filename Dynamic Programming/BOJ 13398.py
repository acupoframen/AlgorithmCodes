import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int,input().split()))
dp=[[0]*2 for _ in range(n)]
dp[0][0]=data[0]
dp[0][1]=data[0]
maxVal=data[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+data[i],data[i])
    dp[i][1]=max(dp[i-1][1]+data[i],dp[i-1][0])
    maxVal=max(dp[i][0],dp[i][1],maxVal)
print(maxVal)