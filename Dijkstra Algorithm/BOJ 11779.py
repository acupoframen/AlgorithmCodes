import heapq
n=int(input())
m=int(input())

data=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
start,end=map(int,input().split())
dist=[1e10 for _ in range(n+1)]
q=[]
heapq.heappush(q,[0,start])
dist[start]=0
answer=1e10
distList=[[i] for i in range(n+1)]
while q:
    currdist,currnum=heapq.heappop(q)
    if currdist>dist[currnum]:
        continue
    if currnum==end:
        if currdist<answer:
            answer=currdist
        continue
    for nextnum,nextval in data[currnum]:
        dist1=currdist+nextval
        if dist1<dist[nextnum]:
            dist[nextnum]=dist1
            heapq.heappush(q,[dist1,nextnum])
            distList[nextnum]=distList[currnum]+[nextnum]
print(answer)
print(len(distList[end]))
print(*distList[end])