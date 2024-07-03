t=int(input())
def dfs(i):
    global answer
    if visited[i]:
        answer+=1
        return
    visited[i]=1
    dfs(data[i])
for _ in range(t):
    n=int(input())
    data=[0]+list(map(int,input().split()))
    visited=[0 for _ in range(n+1)]
    answer=0
    for i in range(1,n+1):
        if visited[i]:
            continue
        dfs(i)
    print(answer)