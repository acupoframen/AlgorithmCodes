import sys
import heapq
input=sys.stdin.readline
v,m=map(int,input().split())
data=list([] for _ in range(v+1))
for _ in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])
j,s=map(int,input().split())

jidist=[1e10 for _ in range(v+1)]
jidist[j]=0
q=[]
heapq.heappush(q,[0,j])
while q:
    currdist,curr=heapq.heappop(q)
    if jidist[curr]<currdist:
        continue
    for next,nextdist in data[curr]:
        if nextdist+currdist<jidist[next]:
            heapq.heappush(q,[nextdist+currdist,next])
            jidist[next]=nextdist+currdist
jidist[j]=1e10
#---
sudist=[1e10 for _ in range(v+1)]
sudist[s]=0
q=[]
heapq.heappush(q,[0,s])
while q:
    currdist,curr=heapq.heappop(q)
    if sudist[curr]<currdist:
        continue
    for next,nextdist in data[curr]:
        if nextdist+currdist<sudist[next]:
            heapq.heappush(q,[nextdist+currdist,next])
            sudist[next]=nextdist+currdist
sudist[s]=1e10

answer=1e10
ji=1e10
curr=0
for i in range(1,v+1):
    if jidist[i]==1e10 or sudist[i]==1e10:
        continue
    if answer>jidist[i]+sudist[i]:
        if jidist[i]<=sudist[i]:
            answer=jidist[i]+sudist[i]
            ji=jidist[i]
            curr=i
    elif answer==jidist[i]+sudist[i]:
        if jidist[i]<=sudist[i] and jidist[i]<ji:
            answer=jidist[i]+sudist[i]
            ji=jidist[i]
            curr=i
if answer==1e10:
    print(-1)
else:
    print(curr)