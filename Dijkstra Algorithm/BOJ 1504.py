import sys
import heapq
input=sys.stdin.readline
n,e=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])
answer=1e10
def dij(a,b):
    dist=[1e10 for _ in range(n+1)]
    dist[a]=0
    q=[]
    heapq.heappush(q,[0,a])
    while q:
        currdist,curr=heapq.heappop(q)
        if dist[curr]<currdist:
            continue
        for next,nextdist in data[curr]:
            if dist[next]>currdist+nextdist:
                dist[next]=currdist+nextdist
                heapq.heappush(q,[dist[next],next])
    
    return dist[b]

a,b=map(int,input().split())

if a==1: 
    answer=dij(1,b)+dij(b,n)
    if answer<1e10:
        print(answer)
    else:
        print(-1)
elif b==n:
    answer=dij(1,a)+dij(a,n)
    if answer<1e10:
        print(answer)
    else:
        print(-1)
else:
    answer=min(dij(1,a)+dij(a,b)+dij(b,n),dij(1,b)+dij(b,a)+dij(a,n)) 
    if answer<1e10:
        print(answer)
    else:
        print(-1)