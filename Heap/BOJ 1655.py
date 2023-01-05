import heapq
import sys
input=sys.stdin.readline
maxHeap=[]
minHeap=[]
n=int(input())
for i in range(n):
    num=int(input())
    if len(maxHeap)==len(minHeap):
        heapq.heappush(minHeap, -1*num)
    else:
        heapq.heappush(maxHeap, num)
    if maxHeap and -minHeap[0]>maxHeap[0]:
        a=heapq.heappop(minHeap)
        b=heapq.heappop(maxHeap)
        heapq.heappush(minHeap,-b)
        heapq.heappush(maxHeap,-a)
    print(-minHeap[0])