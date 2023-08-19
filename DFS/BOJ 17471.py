from collections import deque
from itertools import combinations
def bfs(v):
    q=deque()
    q.append(v[0])
    visited=[-1 for _ in range(n+1)]
    visited[v[0]]=1
    count=1
    total=0
    while q:
        curr=q.popleft()
        total+=people[curr]
        for next in data[curr]:
            if visited[next]==-1 and next in v:
                q.append(next)
                visited[next]=1
                count+=1
    return total,count
n=int(input())
people=[0]+list(map(int,input().split()))
data=[[]]
for _ in range(n):
    __, *a=map(int,input().split())
    data.append(a)

city=[i for i in range(1,n+1)]
answer=1e10
for i in range(1,n//2+1):
    combin=list(combinations(city,i))
    for c in combin:
        total1,count1=bfs(c)
        total2, count2=bfs([j for j in range(1,n+1) if j not in c])
        if count1+count2==n:
            answer=min(answer,abs(total1-total2))
if answer!=1e1:
    print(answer)
else:
    print(-1)