from collections import deque
n,m=map(int,input().split())
truth=list(map(int,input().split()))
truth= truth[1:]
location=[1e10 for _ in range(n+1)]
lines=[[] for _ in range(n+1)]
contests=[]
for _ in range(m):
    a,*b=list(map(int,input().split()))
    contests.append(b)
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            lines[b[i]].append(b[j])
            lines[b[j]].append(b[i])
q=deque()
for i in truth:
    q.append(i)

while q:
    point=q.popleft()
    location[point]=0
    for i in lines[point]:
        if location[i]==1e10:
            q.append(i)
answer=0
truthmust=[i for i in range(1,len(location)) if location[i]==0]
for i in contests:
    okayflag=1
    for j in truthmust:
        if j in i:
            okayflag=0
            break
    if okayflag==1:
        answer+=1
print(answer)