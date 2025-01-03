n=int(input())
data=list(map(int,input().split()))
m=int(input())
marbles=list(map(int,input().split()))
dp=list(list(0 for _ in range(500*i+1)) for i in range(n+1))
def dfs(num,w):
    if num>n:
        return
    if dp[num][w]:
        return
    dp[num][w]=1
    dfs(num+1,w+data[num-1])
    dfs(num+1,w)
    dfs(num+1,abs(w-data[num-1]))
dfs(0,0)

for i in marbles:
    if i>500*n:
        print("N",end=" ")
    elif dp[n][i]:
        print("Y",end=" ")
    else:
        print("N", end=" ")