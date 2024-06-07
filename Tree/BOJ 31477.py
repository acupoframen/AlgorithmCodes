import sys
sys.setrecursionlimit(100002)
n=int(input())
data=list([] for _ in range(n+1))
for _ in range(n-1):
    a,b,v=map(int,input().split())
    data[a].append([b,v])
    data[b].append([a,v])
visited=[0 for _ in range(n+1)]
visited[1]=1
reald=[[] for _ in range(n+1)]
def dfs(a):
    for i,j in data[a]:
        if not visited[i]:
            reald[a].append([i,j])
            visited[i]=1
            dfs(i)
dfs(1)
answer=1e10
def calc(a):
    if len(reald[a])>1:
        temp=0
        for i in range(len(reald[a])):
            temp+=min(calc(reald[a][i][0]),reald[a][i][1])
        return temp
    elif len(reald[a])==1:
        return min(calc(reald[a][0][0]),reald[a][0][1])
    else:
        return 1e10
print(calc(1))