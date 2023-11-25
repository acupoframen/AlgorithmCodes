import heapq
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
data.sort(key= lambda x: x[1])
answer=[]
for p,d in data:
    heapq.heappush(answer,p)
    if len(answer)>d:
        heapq.heappop(answer)

print(sum(answer))