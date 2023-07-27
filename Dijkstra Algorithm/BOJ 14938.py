import sys
input=sys.stdin.readline
import heapq
n,m,r=map(int,input().split())
items=[0]+list(map(int,input().split()))
data=[[] for _ in range(n+1)]
for _ in range(r):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])
answer=0
for i in range(1,n+1):
    temp=0
    q=[]
    dist=[1e10 for _ in range(n+1)]
    heapq.heappush(q,[0,i])
    dist[i]=0
    while q:
        currval,currnum=heapq.heappop(q)
        if currval>dist[currnum]:
            continue
        for nextnum,nextval in data[currnum]:
            newdist=currval+nextval
            if newdist>m:
                continue
            if dist[nextnum]>newdist:
                dist[nextnum]=newdist
                heapq.heappush(q,[newdist,nextnum])
    
    for i in range(1,n+1):
        if dist[i]!=1e10:
            temp+=items[i]
    
    answer=max(answer,temp)
print(answer)