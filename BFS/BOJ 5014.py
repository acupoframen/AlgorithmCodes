from collections import deque
f,s,g,u,d=map(int,input().split())
q=deque()
q.append(s)
data=[1e10 for _ in range(f+1)]
data[s]=0
while q:
    n=q.popleft()
    if n==g:
        break
    if u+n<=f:
        if data[u+n]>data[n]+1:
            data[u+n]=data[n]+1
            q.append(u+n)
    if n-d>=1:
        if data[n-d]>data[n]+1:
            data[n-d]=data[n]+1
            q.append(n-d)
if data[g]==1e10:
    print("use the stairs")
else:
    print(data[g])