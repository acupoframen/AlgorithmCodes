import heapq

n,m=map(int,input().split())
data=list(map(int,input().split()))
heapq.heapify(data)
for i in range(m):
    a=heapq.heappop(data)
    b=heapq.heappop(data)
    heapq.heappush(data,a+b)
    heapq.heappush(data,a+b)

print(sum(data))