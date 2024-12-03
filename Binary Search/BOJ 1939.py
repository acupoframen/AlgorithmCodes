from collections import deque
from collections import defaultdict
import sys
input=sys.stdin.readline

def bfs(w):
    q=deque()
    q.append(start)
    visited=list(0 for _ in range(n+1))
    while q:
        curr=q.popleft()
        for i in data[curr]:
            nextsize=data[curr][i]
            if not visited[i] and nextsize>=w:
                visited[i]=1
                q.append(i)
    if visited[end]:
        return 1
    else:
        return 0


n,m=map(int,input().split())
data=list(defaultdict(int) for _ in range(n+1))
for i in range(m):
    a,b,c=map(int,input().split())
    data[a][b]+=c
    data[b][a]+=c
start,end=map(int,input().split())

left=1
right=int(1e9)

answer=0
while left<=right:
    mid=(left+right)//2
    if bfs(mid):
        answer=mid
        left=mid+1
    else:
        right=mid-1

print(answer)