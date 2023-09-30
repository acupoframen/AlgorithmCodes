from collections import deque
n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
degree=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    degree[b]+=1
    data[a].append(b)
q=deque([])
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)
answer=[]
while q:
    a=q.popleft()
    answer.append(a)
    for i in data[a]:
        degree[i]-=1
        if degree[i]==0:
            q.append(i)

print(*answer)