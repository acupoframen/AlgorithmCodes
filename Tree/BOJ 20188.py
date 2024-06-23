import sys
input=sys.stdin.readline
n=int(input())
data=list(list() for _ in range(n+1))
sys.setrecursionlimit(int(3*1e5)+10)

def dfs(curr):
    global answer
    dist[curr]=1
    for i in data[curr]:
        if not dist[i]:
            dist[curr]+=dfs(i)
    answer+=n*(n-1)//2 - (n-dist[curr])*(n-dist[curr]-1)//2
    return dist[curr]
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
dist=list(0 for _ in range(n+1))
answer=0
dfs(1)

print(int(answer-n*(n-1)//2))