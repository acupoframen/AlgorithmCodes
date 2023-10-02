import sys
sys.setrecursionlimit(10**6)
def movevalue(a,b):
    if a==b:
        return 1
    elif a==0:
        return 2
    elif abs(a-b)==2:
        return 4
    else:
        return 3

data= list(map(int,input().split()))
data.pop()
dp=[[[1e10]*5 for _ in range(5)] for _ in range(len(data)+1)]
dp[0][0][0]=0

for i in range(1,len(data)+1):
    curr=data[i-1]
    for left in range(5):
        for right in range(5):
            dp[i][curr][right]=min(dp[i][curr][right],dp[i-1][left][right]+movevalue(left,curr))
            dp[i][left][curr]=min(dp[i][left][curr],dp[i-1][left][right]+movevalue(right,curr))

answer=1e10
for i in range(5):
    for j in range(5):
        answer=min(answer,dp[len(data)][i][j])

print(answer)