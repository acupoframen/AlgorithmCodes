import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e5))
def dfs(x,d):
    visited[x]=1
    depth[x]=d
    for i in data[x]:
        if visited[i]:
            continue
        parents[i][0]=x
        dfs(i,d+1)
def lca(a,b):
    for i in range(16,-1,-1):
        if depth[a]>depth[b]:
            a,b=b,a
            #makes sure b is bigger
        if depth[b]-depth[a]>=2**i:
            b=parents[b][i]
    if a==b:
        return a
    for i in range(16,-1,-1):
        if parents[a][i]!=parents[b][i]:
            a=parents[a][i]
            b=parents[b][i]
    return parents[a][0]
n=int(input())
data=[list() for _ in range(n+1)]
parents=[list(0 for _ in range(17)) for _ in range(n+1)]
visited=list(0 for _ in range(n+1))
depth=[0 for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
m=int(input())
dfs(1,0)
for j in range(1,n+1):
    for i in range(1,17):
        parents[j][i]=parents[parents[j][i-1]][i-1]
for _ in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))

