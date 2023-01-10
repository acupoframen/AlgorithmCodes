import sys
input=sys.stdin.readline
import heapq
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
location,p=map(int,input().split())
heapq.heapify(data)
possibleGas=[]
answer=0
while p<location:
    while data and data[0][0]<=p:
        heapq.heappush(possibleGas,-heapq.heappop(data)[1])
    if not possibleGas:
        answer=-1
        break
    p+=-(heapq.heappop(possibleGas))
    answer+=1
print(answer)