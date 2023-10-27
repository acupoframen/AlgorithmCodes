from collections import deque
n=int(input())
data=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
answer=[1e10 for i in range(n+1)]
q=deque([1])
while q:
    a=q.popleft()
    for i in data[a]:
        if answer[i]==1e10:
            q.append(i)
            answer[i]=a
for i in range(2,n+1):
    print(answer[i])