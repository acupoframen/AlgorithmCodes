from collections import deque
n=int(input())

q=deque()
for i in range(1,n+1):
    q.append(i)
while q:
    print(q.popleft(),end=" ")
    if q:
        num=q.popleft()
        q.append(num)