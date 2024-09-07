from collections import defaultdict 
import heapq
n,m,k=map(int,input().split())
data=defaultdict(int)
firstq=[]
secondq=[]
for i in range(n):
    a,b=map(int,input().split())
    data[a]=0
    heapq.heappush(firstq,[-a,-b])
    heapq.heappush(secondq,[-b,-a])

answer=0
while k>0:
    b,a=heapq.heappop(secondq)
    b*=-1
    a*=-1
    data[a]=1
    answer+=a
    k-=1

while m>0:
    a,b=heapq.heappop(firstq)
    a*=-1
    b*=-1
    if data[a]==0:
        data[a]=1
        answer+=a
        m-=1

print(answer)