t=int(input())
dp=list(0 for _ in range(100001))
answer=list(0 for _ in range(100001))
dp[1]=1
dp[2]=2
dp[3]=4
answer[1]=1
answer[2]=2
answer[3]=2
for i in range(4,100001):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i]%=1000000009
    if not i%2:
        answer[i]=dp[i//2]+dp[(i-2)//2]
    else:
        answer[i]=dp[(i-1)//2]+dp[(i-3)//2]
    
for _ in range(t):
    n=int(input())
    print(answer[n]%1000000009)