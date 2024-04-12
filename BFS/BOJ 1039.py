from collections import deque
n,k=map(int,input().split())
m=len(str(n))
visited=set()
visited.add((n,0))
q=deque()
q.append([n,0])
answer=0
while q:
    n,count=q.popleft()
    if count==k:
        answer=max(answer,n)
        continue
    num=list(str(n))
    for i in range(m-1):
        for j in range(i+1,m):
            if not i and num[j]=='0':
                continue
            num[i],num[j]=num[j],num[i]
            newn=int(''.join(num))
            if (newn,count+1) not in visited:
                q.append([newn,count+1])
                visited.add((newn,count+1))
            num[i],num[j]=num[j],num[i]
if answer:
    print(answer)
else:
    print(-1)