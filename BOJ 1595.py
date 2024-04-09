from collections import deque

data=list([] for _ in range(10001))
while True:
    try:
        a,b,c=map(int,input().split())
        data[a].append([b,c])
        data[b].append([a,c])
    except:
        break

dist=list(-1 for _ in range(10001))
q=deque()
q.append(1)
while q:
    a=q.popleft()
    dist[a]=0
    for i,j in data[a]:
        if dist[i]==-1:
            dist[i]=dist[a]+j
            q.append(i)

a=dist.index(max(dist))
dist=list(-1 for _ in range(10001))
q=deque()
q.append(a)
while q:
    a=q.popleft()
    dist[a]=0
    for i,j in data[a]:
        if dist[i]==-1:
            dist[i]=dist[a]+j
            q.append(i)
print(max(dist))