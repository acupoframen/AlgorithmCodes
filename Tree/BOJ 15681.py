import sys
sys.setrecursionlimit(int(1e5+2))
input=sys.stdin.readline

n,r,q=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    data[u].append(v)
    data[v].append(u)

dp=[0 for _ in range(n+1)]


def dfs(i):
    dp[i]=1
    for j in data[i]:
        if not dp[j]:
            dp[i]+=dfs(j)
    return dp[i]

dfs(r)

for _ in range(q):
    i=int(input())
    print(dp[i])