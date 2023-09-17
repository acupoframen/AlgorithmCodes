t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    m=int(input())

    dp=[0 for _ in range(m+1)]
    dp[0]=1
    for i in data:
        for j in range(m-i+1):
            dp[i+j]+=dp[j]
    print(dp[m])