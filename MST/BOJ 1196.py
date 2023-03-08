import sys
import heapq
input=sys.stdin.readline
v,e=map(int,input().split())
parent=[i for i in range(v+1)]
edges=[]
for i in range(e):
    a,b,v=map(int,input().split())
    heapq.heappush(edges,[v,a,b])
def find(n):
    if n!=parent[n]:
        parent[n]=find(parent[n])
    return parent[n]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a>b:
            parent[a]=b
        else:
            parent[b]=a
answer=0
while edges:
    v,a,b=heapq.heappop(edges)
    pa=find(a)
    pb=find(b)
    if pa!=pb:
        answer+=v
        union(a,b)
print(answer)