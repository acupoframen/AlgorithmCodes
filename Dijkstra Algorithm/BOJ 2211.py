import heapq
n,m=map(int,input().split())
distance=[1e10 for _ in range(n+1)]
parent=[0 for _ in range(n+1)]
data=list(list() for _ in range(n+1))
for _ in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])
q=[]
distance[1]=0
heapq.heappush(q,[0,1])
while q:
    dist,curr=heapq.heappop(q)
    if distance[curr]<dist:
        continue
    for next,nextdist in data[curr]:
        temp=dist+nextdist
        if distance[next]>temp:
            parent[next]=curr
            distance[next]=temp
            heapq.heappush(q,[temp,next])
print(n-1)
for i in range(2,n+1):
    print(i,parent[i])