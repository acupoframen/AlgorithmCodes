from collections import deque
import sys
input=sys.stdin.readline
def bfs(start):
    visited=[-1 for _ in range(n+1)]
    visited[start]=0
    q=deque()
    q.append([start,0])
    maximumVal=[0,0]
    while q:
        origin,dist=q.popleft()
        for next,value in tree[origin]:
            if visited[next]==-1:
                visited[next]=dist+value
                q.append([next,visited[next]])
                if maximumVal[1]<visited[next]:
                    maximumVal=[next,visited[next]]
    return maximumVal
n=int(input())
data=[list(map(int,input().split())) for _ in range(n-1)]
tree=[[] for _ in range(n+1)]
for a,b,num in data:
    tree[a].append([b,num])
    tree[b].append([a,num])
node,distance=bfs(1)
node,distance=bfs(node)
print(distance)