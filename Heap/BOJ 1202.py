import sys
import heapq
input= sys.stdin.readline
n,k=map(int,input().split())
weightandvalue=[list(map(int,input().split())) for _ in range(n)]
maxweight=[int(input()) for _ in range(k)]
weightandvalue.sort()
temp=[]
answer=0
for bag in maxweight:
    while weightandvalue and weightandvalue[0][0]<=bag:
        print(maxweight)
        print(weightandvalue)
        heapq.heappush(temp,-heapq.heappop(weightandvalue)[1])
    if temp:
        answer-=(heapq.heappop(temp))
print(answer)