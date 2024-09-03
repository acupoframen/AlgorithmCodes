import sys
import math

sys.setrecursionlimit(int(5e4))
input = sys.stdin.readline

n = int(input())
LOG = math.ceil(math.log2(n))
data = [[] for _ in range(n+1)]
parent = [-1] * (n+1)
depth = [0] * (n+1)
up = [[-1] * (LOG + 1) for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

def dfs(v, p):
    parent[v] = p
    depth[v] = depth[p] + 1
    up[v][0] = p
    for i in range(1, LOG + 1):
        if up[v][i-1] != -1:
            up[v][i] = up[up[v][i-1]][i-1]
    
    for to in data[v]:
        if to != p:
            dfs(to, v)

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    
    # u를 v와 같은 깊이로 맞추기
    for i in range(LOG, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = up[u][i]
    
    if u == v:
        return u
    
    # u와 v를 동시에 올려 공통 조상 찾기
    for i in range(LOG, -1, -1):
        if up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
    
    return parent[u]

dfs(1, 0)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v))
