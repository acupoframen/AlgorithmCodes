import sys
input=sys.stdin.readline
from collections import deque
import heapq
n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])

dist=[1e10 for _ in range(n+1)]

q=list()

q.append([0,1])
dist[1]=0
while q:
    currdist,currnum=heapq.heappop(q)
    if dist[currnum]>currdist:
        continue
    for nextnum,nextdist in data[currnum]:
        dist1=currdist+nextdist
        if dist[nextnum]>dist1:
            dist[nextnum]=dist1
            q.append([dist1,nextnum])

print(dist[n])
