import sys
sys.setrecursionlimit(1000001)
input=sys.stdin.readline
n=int(input())
data=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
visited=[0 for _ in range(n+1)]
dp=[[0,0] for _ in range(n+1)]
def dfs(num):
    visited[num]=1
    dp[num][0]=0
    dp[num][1]=1
    for i in data[num]:
        if visited[i]:
            continue
        dfs(i)
        dp[num][0]+=dp[i][1]
        dp[num][1]+=min(dp[i][1],dp[i][0])

dfs(1)
print(min(dp[1]))