n=int(input())
data=list(map(int, input().split()))
visited=list(0 for _ in range(17))
data.sort()
answer=[-1 for _ in range(n*2)]
def dfs(idx):
    if idx==n*2:
        print(*answer)
        exit(0)
    if answer[idx]!=-1:
        dfs(idx+1)
        return
    for i in range(n):
        num=data[i]
        nextidx=idx+num+1
        if not visited[num]:
            if 0<=nextidx<n*2 and answer[nextidx]==-1:
                visited[num]=1
                answer[idx]=num
                answer[nextidx]=num
                dfs(idx+1)
                visited[num]=0
                answer[idx]=-1
                answer[nextidx]=-1
dfs(0)
print(-1)