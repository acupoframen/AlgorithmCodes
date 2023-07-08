import sys
import heapq

input=sys.stdin.readline
n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
degree=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    degree[b]+=1

q=[]
for i in range(1,n+1):
    if degree[i]==0:
        heapq.heappush(q,i)

while q:
    a=heapq.heappop(q)
    print(a, end=' ')
    if data[a]:
        for j in data[a]:
            degree[j]-=1
            if degree[j]==0:
                heapq.heappush(q,j)
    