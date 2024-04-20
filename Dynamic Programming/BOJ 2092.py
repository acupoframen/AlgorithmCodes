t,a,s,b=map(int,input().split())
data=list(map(int,input().split()))
answer=0
dp=[[0 for _ in range(4001)] for _ in range(201)]
num=[0 for _ in range(201)]
for i in range(a):
    num[data[i]]+=1
for i in range(1,t+1):
    for j in range(num[i]+1):
        dp[i][j]+=1
    for j in range(1,a+1):
        dp[i][j]+=dp[i-1][j]
        for k in range(1,num[i]+1):
            if j>k:
                dp[i][j]+=dp[i-1][j-k]
                dp[i][j]%=1000000

for i in range(s,b+1):
    answer+=dp[t][i]%1000000
print(answer%1000000)