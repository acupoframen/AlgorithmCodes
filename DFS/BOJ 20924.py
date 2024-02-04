import sys
sys.setrecursionlimit(int(2*1e5+2))
from collections import deque
n,r=map(int,input().split())
data=list([] for _ in range(n+1))
for _ in range(n-1):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])
q=deque([r])
giga=0
answer1=0
visited=[0 for _ in range(n+1)]
visited[r]=1
while q:
    a=q.popleft()
    if 1<=len(data[a])<=2:
        if len(data[a])==2 and a==r:
            giga=r
            break
        for i,j in data[a]:
            if not visited[i]:
                q.append(i)
                answer1+=j
                visited[i]=1
    else:
        giga=a
        break
answer2=0
def dfs(a,d):
    global answer2
    answer2=max(answer2,d)
    for b,dist in data[a]:
        if not visited[b]:
            visited[b]=1
            dfs(b,d+dist)
    return 
dfs(giga,0)
print(answer1, answer2)