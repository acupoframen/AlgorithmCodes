from collections import deque

n,k=map(int,input().split())

q=deque([i for i in range(1,n+1)])

while len(q)!=1:
    a=q.popleft()
    q.append(a)
    for i in range(k-1):
        q.popleft()
        if len(q)==1:
            print(q.popleft())
            exit(0)
print(q[0])