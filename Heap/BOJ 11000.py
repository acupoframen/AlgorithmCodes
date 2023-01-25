import heapq
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
data.sort()
q=[]
for i in data:
    if q:
        if q[0]<=i[0]:
            heapq.heappop(q)
    heapq.heappush(q,i[1])
print(len(q))