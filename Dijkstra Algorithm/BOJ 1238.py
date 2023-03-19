import sys
import heapq
input=sys.stdin.readline
n,m,x=map(int,input().split())
d_x=[1e10 for _ in range(n+1)]
roadData=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    roadData[a].append([b,c])
def dijkstra(num):
    d=[1e10 for _ in range(n+1)]
    d[num]=0
    q=[]
    heapq.heappush(q,[0,num])
    while q:
        dist,oldCoord=heapq.heappop(q)
        if dist>d[oldCoord]:
            continue
        for where,value in roadData[oldCoord]:
            if d[where]>value+d[oldCoord]:
                d[where]=value+d[oldCoord]
                heapq.heappush(q,[d[where],where])
    return d
answer=0
d_x=dijkstra(x)
for i in range(1,n+1):
    answer=max(answer,dijkstra(i)[x]+d_x[i])
print(answer)