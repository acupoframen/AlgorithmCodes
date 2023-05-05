from collections import deque
n=int(input())
m=int(input())
data=list(map(int,input().split()))
data.sort()
q=deque(data)
answer=0
while q:
    if len(q)==1:
        break
    a,b=q.popleft(),q.pop()
    if a+b==m:
        answer+=1
    elif a+b<m:
        q.append(b)
    else:
        q.append(a)
print(answer)
