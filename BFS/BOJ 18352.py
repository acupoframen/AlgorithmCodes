from collections import deque
n,m,k,x=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)

dist=[1e10 for _ in range(n+1)]
dist[x]=0
q=deque()
q.append(x)
answer=[]
while q:
    node=q.popleft()
    if dist[node]==k:
        answer.append(node)
        continue
    for i in data[node]:
        if dist[node]+1<dist[i]:
            q.append(i)
            dist[i]=dist[node]+1

if not len(answer):
    print(-1)
else:
    for i in sorted(answer):
        print(i)