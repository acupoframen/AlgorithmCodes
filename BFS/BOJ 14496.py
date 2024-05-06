from collections import deque
a,b=map(int,input().split())
n,m=map(int,input().split())
data=list(list() for _ in range(n+1))
for _ in range(m):
    x,y=map(int,input().split())
    data[x].append(y)
    data[y].append(x)
visited=[0 for _ in range(n+1)]
q=deque()
q.append([a,0])
visited[a]=1
while q:
    num,val=q.popleft()
    if num==b:
        print(val)
        exit(0)
    for i in data[num]:
        if not visited[i]:
            visited[i]=val+1
            q.append([i,val+1])
print(-1)