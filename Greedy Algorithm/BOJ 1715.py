import sys
import heapq
input=sys.stdin.readline
n=int(input())
data=[int(input()) for _ in range(n)]
heapq.heapify(data)
answer=0
while len(data)!=1:
    number=0
    for i in range(2):
        number+=heapq.heappop(data)
    answer+=number
    heapq.heappush(data,number)
print(answer)