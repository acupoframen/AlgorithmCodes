n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
data.sort(key= lambda x: x[0])

dp=[1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if data[j][1]<data[i][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))