from collections import deque
n,m=map(int,input().split())
data=list([] for _ in range(n+1))
def dfs(a,count):
    if count==4:
        print(1)
        exit(0)
    for i in data[a]:
        if not visited[i]:
            visited[i]=1
            dfs(i,count+1)
            visited[i]=0
for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(n):
    visited=[0 for _ in range(n)]
    visited[i]=1
    dfs(i,0)
print(0)