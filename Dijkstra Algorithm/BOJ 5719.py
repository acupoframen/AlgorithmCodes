import heapq
import sys
input=sys.stdin.readline
def dijk(v):
    minlen[v]=0
    q=[]
    q.append([0,v])
    while q:
        currdist,curr=heapq.heappop(q)
        if minlen[curr]<currdist:
            continue
        for next,nextdist in data[curr]:
            if nextdist+currdist<minlen[next] and not check[curr][next]:
                minlen[next]=nextdist+currdist
                heapq.heappush(q,[minlen[next],next])
def dijk2(v):
    q=[]
    q.append([minlen[v],v])
    while q:
        currdist,curr=heapq.heappop(q)
        if curr==s:
            continue
        for past, pastdist in data2[curr]:
            if check[past][curr]:
                continue
            if minlen[past]==minlen[curr]-pastdist:
                check[past][curr]=1
                heapq.heappush(q,[minlen[past],past])

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    s,d=map(int,input().split())
    data=list(list() for _ in range(n+1))
    data2=list(list() for _ in range(n+1))
    check=list(list(0 for _ in range(n+1)) for _ in range(n+1))
    minlen=list(1e10 for _ in range(n+1))
    for _ in range(m):
        u,v,p=map(int,input().split())
        data[u].append([v,p])
        data2[v].append([u,p])
    dijk(s)
    dijk2(d)
    for i in range(n+1):
        minlen[i]=1e10
    dijk(s)
    if minlen[d]==1e10:
        print(-1)
    else:
        print(minlen[d])