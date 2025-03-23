t=int(input())
dp=list(list(0 for _ in range(211)) for _ in range(21))
dp[1][0]=1
dp[1][1]=1
for i in range(2,21):
    for j in range(i*(i+1)//2+1):
        for k in range(max(0,j-i),j+1):
            dp[i][j]+=dp[i-1][k]

for _ in range(t):
    k,n=map(int,input().split())
    print(dp[k][n])