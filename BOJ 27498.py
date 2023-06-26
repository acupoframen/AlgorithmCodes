import sys
input=sys.stdin.readline
import heapq
n,m=map(int,input().split())
totalSum=0
data=[]
parents=[x for x in range(n+1)]
q=[]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b
for _ in range(m):
    a,b,c,d=map(int,input().split())
    if d:
        union(a,b)
    else:
        heapq.heappush(q,[-c,a,b])
        totalSum+=c


while q:
    val,a,b=heapq.heappop(q)
    if find(a)!=find(b):
        union(a,b)
        totalSum+=val
print(totalSum)