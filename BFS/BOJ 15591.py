import sys
from collections import deque
input=sys.stdin.readline
n,q=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,r=map(int,input().split())
    data[a].append([b,r])
    data[b].append([a,r])

for _ in range(q):
    a,b=map(int,input().split())
    visited=[0]*(n+1)
    visited[b]=1
    answer=0
    q=deque()
    q.append([b,1e12])
    while q:
        curr, val=q.popleft()
        for next, nextval in data[curr]:
            nextval=min(nextval,val)
            if nextval>=a and not visited[next]:
                answer+=1
                q.append([next,nextval])
                visited[next]=1
    print(answer)
