from collections import deque
n,k,m=map(int,input().split())
data=list(list() for _ in range(n+1))
hypertube=list(list() for _ in range(m))
for i in range(m):
    temp=list(map(int,input().split()))
    for j in temp:
        data[j].append(i)
        hypertube[i].append(j)
if n==1:
    print(1)
    exit(0)
visited=[0]*(n+1) #stations
visitedhyper=[0]*m #hypertubes
q=deque()
q.append([1,1])
visited[1]=1
while q:
    curr,count=q.popleft()
    next=[]
    for i in data[curr]:
        if not visitedhyper[i]:
            visitedhyper[i]=1
            next.append(i)
    for i in next:
        for j in hypertube[i]:
            if not visited[j]:
                if j==n:
                    print(count+1)
                    exit(0)
                visited[j]=1
                q.append([j,count+1])
print(-1)