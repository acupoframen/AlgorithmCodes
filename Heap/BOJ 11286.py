from heapq import *
import sys
input=sys.stdin.readline
n=int(input())
heap=[]
for _ in range(n):
    n=int(input())
    if n==0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap,(abs(n),n))
