import sys
n=int(input())
sys.setrecursionlimit(int(6e4))
data=[[] for _ in range(n+1)]
parent=[1e10 for _ in range(n+1)]
depth=[0 for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
parent[1]=1
def dfs(x,d):
    depth[x]=d
    for i in data[x]:
        if parent[i]!=1e10:
            continue
        parent[i]=x
        dfs(i,d+1)

def lca(a,b):
    while depth[a]!=depth[b]:
        if depth[a]>depth[b]:
            a=parent[a]
        else:
            b=parent[b]
    while a!=b:
        a=parent[a]
        b=parent[b]
    
    return a


dfs(1,0)
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))