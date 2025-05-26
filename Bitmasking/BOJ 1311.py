n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
visited=list(list(-1 for _ in range(1<<n)) for _ in range(n))
def dfs(d,visit):
    if d==n:
        return 0
    if visited[d][visit]!=-1:
        return visited[d][visit]
    temp=int(1e10)
    for i in range(n):
        if visit&(1<<i):
            continue
        temp=min(temp,dfs(d+1,(visit|(1<<i)))+data[d][i])
    visited[d][visit]=temp
    return temp
print(dfs(0,0)) 