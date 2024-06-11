from collections import deque
n=int(input())
data=list(list() for _ in range(n+1))
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    data[a].append(b)
    data[b].append(a)
answer=[]
for i in range(1,n+1):    
    q=deque()
    visited=[0 for _ in range(n+1)]
    q.append([i,0])
    visited[i]=1
    temp=0
    while q:
        x,dist=q.popleft()
        for j in data[x]:
            if not visited[j]:
                visited[j]=1
                temp=max(temp,dist+1)
                q.append([j,dist+1])
    answer.append([i,temp])
answer.sort(key=lambda x:x[1])
score=answer[0][1]
ppl=[]
for i in range(len(answer)):
    if answer[i][1]==score:
        ppl.append(answer[i][0])
    else:
        break
print(score,len(ppl))
print(*ppl)