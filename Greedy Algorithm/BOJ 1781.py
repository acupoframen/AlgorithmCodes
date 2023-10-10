import sys
import heapq
input=sys.stdin.readline
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]

data.sort()
q=[]
for i in data:
    heapq.heappush(q,i[1])
    if i[0]<len(q):
        heapq.heappop(q)

print(sum(q))