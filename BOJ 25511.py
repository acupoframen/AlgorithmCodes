from collections import deque
n,k=map(int,input().split())
data=list([] for _ in range(n))
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
val=list(0 for _ in range(n))
idx=list(map(int,input().split()))
goal=idx.index(k)
q=deque()
q.append([0,0])
while q:
    curr,d=q.popleft()
    if curr==goal:
        print(d)
        break
    for i in data[curr]:
        if not val[i]:
            val[i]=1
            q.append([i,d+1])
