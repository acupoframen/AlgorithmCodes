import sys
input=sys.stdin.readline
import heapq
import math

sieve=[1 for _ in range(int(1e7)+1)]
sieve[1]=0
for i in range(2,int(1e7**0.5)+1):
    if sieve[i]:
        for j in range(2*i,int(1e7)+1,i):
            sieve[j]=0
n,m=map(int,input().split())
busstop=[0]+list(map(int,input().split()))
data=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])

answer=[math.inf for _ in range(n+1)]
answer[1]=0
q=[]
heapq.heappush(q,[0,1])
while q:
    a,b=heapq.heappop(q)
    if answer[b]<a:
        continue
    if b==n:
        print(a)
        exit(0)
    for i,dist in data[b]:
        if sieve[busstop[b]+busstop[i]]==1:
            if a+dist<answer[i]:
                answer[i]=a+dist
                heapq.heappush(q,[a+dist,i])

print("Now where are you?")