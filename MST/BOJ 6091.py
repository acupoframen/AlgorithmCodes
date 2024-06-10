import heapq
n=int(input())
q=[]
for i in range(1,n):
    temp=list(map(int,input().split()))
    for j in range(i+1,n+1):
        heapq.heappush(q,[temp[j-i-1],i,j])

connected=list(list() for _ in range(n+1))
parents=list(i for i in range(n+1))

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

while q:
    dist,a,b=heapq.heappop(q)
    if find(parents[a])!=find(parents[b]):
        union(a,b)
        connected[a].append(b)
        connected[b].append(a)
for i in connected[1:]:
    print(len(i),*sorted(i))