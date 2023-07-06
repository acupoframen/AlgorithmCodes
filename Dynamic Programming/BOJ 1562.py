n=int(input())
answer=0
mod=1000000000
dp=[[[0 for _ in range(2**10)] for _ in range(10)] for _ in range(n+1)]
for k in range(1,10):
    dp[1][k][1<<k]=1

for i in range(n):
    for j in range(10):
        for k in range(1024):
            if j<9:
                newBit= k | (1<<(j+1))
                dp[i+1][j+1][newBit]+=dp[i][j][k]
                dp[i+1][j+1][newBit]%=mod
            if j>0:
                newBit=k|(1<<(j-1))
                dp[i+1][j-1][newBit]+=dp[i][j][k]
                dp[i+1][j-1][newBit]%=mod
for i in range(10):
    answer+=dp[n][i][1023]
    answer%=mod
print(answer)