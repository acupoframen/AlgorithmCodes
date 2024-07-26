import sys, heapq
input=sys.stdin.readline
n=int(input())
data=sorted(list(map(int,input().split())) for _ in range(n))
h=[]
for start, end in data:
    if h and h[0]<=start:
        heapq.heappop(h)
    heapq.heappush(h,end)
print(len(h))