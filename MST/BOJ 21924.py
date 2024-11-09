import sys
sys.setrecursionlimit(int(1e5)+1)
import heapq
n,m=map(int,input().split())
parents=[i for i in range(n+1)]
q=[]
totalsum=0
for i in range(m):
    a,b,c=map(int,input().split())
    heapq.heappush(q,[c,a,b])
    totalsum+=c

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

while q:
    num,a,b=heapq.heappop(q)
    if find(parents[a])==find(parents[b]):
        continue
    else:
        union(a,b)
        totalsum-=num

temp=parents[1]
for i in range(2,n+1):
    if find(parents[i])!=temp:
        print(-1)
        exit(0)
print(totalsum)