import heapq
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    k=int(input())
    maxq=[]
    minq=[]
    visited=[0 for _ in range(k)]
    for i in range(k):
        a,b=input().split()
        if a=="I":
            heapq.heappush(maxq,[-int(b),i])
            heapq.heappush(minq,[int(b),i])
            visited[i]=True
        else:
            if b=="1":
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                if maxq:
                    visited[maxq[0][1]]=False
                    heapq.heappop(maxq)
            else:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]]=False
                    heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    if not maxq and not minq:
        print("EMPTY")
    else:
        print(-maxq[0][0],minq[0][0])