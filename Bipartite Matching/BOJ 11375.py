import sys
sys.setrecursionlimit(int(1e5))
n,m=map(int,input().split())
data=list(list(map(int,input().split()))[1:] for _ in range(n))

def dfs(x):
    for i in data[x]:
        if not check[i]:
            check[i]=1
            if visited[i]==-1 or dfs(visited[i]):
                visited[i]=x
                return 1
    return 0

visited=[-1 for _ in range(m+1)]
answer=0
for i in range(n):
    check=[0 for _ in range(m+1)]
    if dfs(i):
        answer+=1

print(answer)