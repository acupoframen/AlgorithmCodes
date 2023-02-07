import heapq
import sys
input=sys.stdin.readline
v,e=map(int,input().split())
start=int(input())
data=[[] for _ in range(v+1)]
values=[1e10]*(v+1)
for _ in range(e):
    a,b,val=map(int,input().split())
    data[a].append([b,val])

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    values[start]=0
    while q:
        val,now=heapq.heappop(q)
        for i in data[now]:
            cost=val+i[1]
            if cost<values[i[0]]:
                values[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1,v+1):
    if values[i]==1e10:
        print("INF")
    else:
        print(values[i])