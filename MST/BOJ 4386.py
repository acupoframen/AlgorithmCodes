import sys
input=sys.stdin.readline
import heapq
import math
edges=[]
n=int(input())
points=[list(map(float,input().split())) for _ in range(n)]
parent=[i for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        d=round(math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2),2)
        heapq.heappush(edges,[d,i,j])
def find(n):
    if parent[n]!=n:
        parent[n]=find(parent[n])
    return parent[n]
def union(a,b):
    pa=find(a)
    pb=find(b)
    if pa!=pb:
        if pa>pb:
            parent[pa]=pb
        else:
            parent[pb]=pa
answer=0
while edges:
    val,a,b=heapq.heappop(edges)
    if find(a)!=find(b):
        union(a,b)
        answer+=val
print(round(answer,2))