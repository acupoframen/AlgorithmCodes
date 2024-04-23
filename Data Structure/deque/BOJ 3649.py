from collections import deque
n,k=map(int,input().split())
data=list(map(int,input().split()))
q=deque()
for i in range(n):
    while q and q[-1][0]> data[i]:
        q.pop()
    while q and q[0][1]<i-k+1:
        q.popleft()
    q.append([data[i],i])
    print(q[0][0],end=" ")