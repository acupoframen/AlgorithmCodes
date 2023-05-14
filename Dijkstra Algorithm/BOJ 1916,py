import heapq
n=int(input())
m=int(input())
road=[[] for _ in range(n+1)]
coords=[1e10 for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    road[a].append([b,c])
q=[]
start,end=map(int,input().split())
coords[start]=0
heapq.heappush(q,[0,start])
while q:
    val,coord=heapq.heappop(q)
    if coords[coord]<val:
        continue
    for newCoord,newVal in road[coord]:
        if coords[newCoord]>newVal+val:
            coords[newCoord]=newVal+val
            heapq.heappush(q,[newVal+val,newCoord])

print(coords[end])