from collections import deque
from copy import deepcopy
n,m=map(int,input().split())
q=deque([i for i in range(1,n+1)])
data=list(map(int,input().split()))
answer=0
for i in data:
    temp1=0
    temp2=1
    q1=deepcopy(q)
    q2=deepcopy(q)
    while True:
        a=q1.popleft()
        if i==a:
            break
        else:
            temp1+=1
            q1.append(a)
    while True:
        a=q2.pop()
        if i==a:
            break
        else:
            temp2+=1
            q2.appendleft(a)
    if temp1<temp2:
        q=q1
        answer+=temp1
    else:
        q=q2
        answer+=temp2

print(answer)