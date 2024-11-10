import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(2e5))
n,m,r=map(int,input().split())
data=list(list() for _ in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
for i  in range(1,n+1):
    data[i].sort(reverse=True)
visited=list(0 for _ in range(n+1))
idx=1
def dfs(x):
    global idx
    visited[x]=idx
    idx+=1
    for i in data[x]:
        if not visited[i]:
            dfs(i)
dfs(r)
for i in range(1,n+1):
    print(visited[i])