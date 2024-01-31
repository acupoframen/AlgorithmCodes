from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list([] for _ in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[b].append(a)
answer=0
answerlist=[]
for i in range(1,n+1):
    q=deque()
    q.append(i)
    temp=0
    visited=[0 for _ in range(n+1)]
    while q:
        num=q.popleft()
        temp+=1
        visited[num]=1
        for j in data[num]:
            if not visited[j]:
                q.append(j)
                visited[j]=1
    if temp>answer:
        answerlist=[i]
        answer=temp
    elif temp==answer:
        answerlist.append(i)
print(*sorted(answerlist))