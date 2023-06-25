import heapq
import sys 
input=sys.stdin.readline
n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])
a,b=map(int,input().split())
home=list(map(int,input().split()))
cvs=list(map(int,input().split()))
purpose=[0]*n
for i in home:
    purpose[i]=1  # HOME
for i in cvs:
    purpose[i]=2 # CONVIENIENT
q=[(n,0)]
values=[1e10]*(n+1)
while q:
    coord,val=heapq.heappop(q)
    if 