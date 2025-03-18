import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list() for _ in range(n+1))
for _ in range(m):
    x,y,d,t=map(int,input().strip().split())
    data[x].append([y,d,t])
    data[y].append([x,d,t]) #node, length, collapsetim
left=0
right=int(1e9)
answer=-1
def dijk(k):
    global answer
    q=[]
    time=list(1e10 for _ in range(n+1))
    time[1]=k
    heapq.heappush(q,[k,1]) #time,node
    while q:
        currtime,curr=heapq.heappop(q)
        if currtime>time[curr]:
            continue
        for next,length,collapsetime in data[curr]:
            if currtime+length>collapsetime:
                continue
            if currtime+length<time[next]:
                heapq.heappush(q,[currtime+length,next])
                time[next]=currtime+length
    if time[n]==1e10:
        return 0
    else:
        return 1

while left<=right:
    mid=(left+right)//2
    if dijk(mid):
        left=mid+1
        answer=max(answer,mid)
    else:
        right=mid-1

print(answer)