from collections import deque
n,m=map(int,input().split())

data=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])

for i in range(m):
    a,b=map(int,input().split())
    q=deque()
    q.append([a,0])
    visited=[0 for _ in range(n+1)]
    visited[a]=1
    while q:
        new,d=q.popleft()
        if new==b:
            print(d)
            break
        for i, l in data[new]:
            if not visited[i]:
                visited[i]=1
                q.append([i,d+l])
    