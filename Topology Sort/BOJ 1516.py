from collections import deque
n=int(input())
data=list([] for _ in range(n+1))
cost=[0 for _ in range(n+1)]
indegree=[0 for _ in range(n+1)]
for i in range(1,n+1):
    a,*b=list(map(int,input().split()))[:-1]
    cost[i]=a
    for j in b:
        data[j].append(i)
        indegree[i]+=1

answer=[0 for _ in range(n+1)]
q=deque()
for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
while q:
    now=q.popleft()
    answer[now]+=cost[now]
    for i in data[now]:
        indegree[i]-=1
        answer[i]=max(answer[i],answer[now])
        if not indegree[i]:
            q.append(i)
for i in range(1,n+1):
    print(answer[i])