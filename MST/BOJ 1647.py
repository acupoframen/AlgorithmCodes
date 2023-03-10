import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=[]
parent=[i for i in range(n+1)]
for _ in range(m):
    a,b,v=map(int,input().split())
    heapq.heappush(data,[v,a,b])
def find(n):
    if parent[n]!=n:
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
answer=[]
while data:
    v,a,b=heapq.heappop(data)
    if find(a)==find(b):
        pass
    else:
        union(a,b)
        answer.append(v)
print(sum(answer)-max(answer))