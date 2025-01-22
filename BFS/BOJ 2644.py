from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
parents=list(list() for _ in range(n+1))
for _ in range(m):
    x,y=map(int,input().split())
    parents[x].append(y)
    parents[y].append(x)
length=[-1 for _ in range(n+1)]
length[a]=0
q=deque()
q.append([a,0])
while q:
    curr,currdist=q.popleft()
    for i in parents[curr]:
        if length[i]==-1:
            length[i]=currdist+1
            q.append([i,currdist+1])

print(length[b])