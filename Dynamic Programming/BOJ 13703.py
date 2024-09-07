k,n=map(int,input().split())
dp=list(list(-1 for _ in range(150)) for _ in range(150))

def f(time,loc):
    if dp[time][loc]!=-1:
        return dp[time][loc]
    if loc==0:
        dp[time][loc]=2**time
        return 2**time
    if time==0:
        return 0
    dp[time][loc]=f(time-1,loc-1)+f(time-1,loc+1)
    return dp[time][loc]
f(n,k)
print(2**n-dp[n][k])
