n=int(input())
weight=[0]+list(map(int,input().split()))
data=list(list() for _ in range(n+1))
dp=[[0,0] for _ in range(n+1)]
path=[[[] for _ in range(2)] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
visited=list(0 for _ in range(n+1))

def dfs(node):
    visited[node]=1
    dp[node][1]+=weight[node]
    path[node][1].append(node)
    for i in data[node]:
        if not visited[i]:
            temp=dfs(i)
            dp[node][0]+=max(dp[i][0],dp[i][1])
            dp[node][1]+=dp[i][0]
            path[node][1]+=temp[0]
            if dp[i][0]>dp[i][1]:
                path[node][0]+=temp[0]
            else:
                path[node][0]+=temp[1]
    return path[node]
answer=dfs(1)
if dp[1][0]>dp[1][1]:
    print(dp[1][0])
    print(*sorted(answer[0]))
else:
    print(dp[1][1])
    print(*sorted(answer[1]))