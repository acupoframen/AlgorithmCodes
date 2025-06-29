import sys
import heapq
input=sys.stdin.readline

def dijk(graph,start,n):
    dist=[int(1e10)]*(n+1)
    dist[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        currcost,curr=heapq.heappop(q)
        if currcost>dist[curr]:
            continue
        for nextcost,next in graph[curr]:
            if dist[next]>currcost+nextcost:
                dist[next]=currcost+nextcost
                heapq.heappush(q,(dist[next],next))
    return dist

T=int(input())
for _ in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    data=list(list() for _ in range(n+1))
    gh=0
    for _ in range(m):
        a,b,d=map(int,input().split())
        data[a].append((d,b))
        data[b].append((d,a))
        if (a==g and b==h) or (a==h and b==g):
            gh=d
    cand=list(int(input())  for _ in range(t))
    answer=[]
    dists=dijk(data,s,n)
    distg=dijk(data,g,n)
    disth=dijk(data,h,n)

    for d in cand:
        path1 = dists[g] + gh + disth[d]
        path2 = dists[h] + gh + distg[d]
        if dists[d] == path1 or dists[d] == path2:
            answer.append(d)
    print(*sorted(answer))
