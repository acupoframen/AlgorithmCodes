import sys
input=sys.stdin.readline
import heapq
n=int(input())
data=[]
for _ in range(n):
    data.append(sorted(list(map(int,input().split()))))
d=int(input())
roadlength=[]
for i in data:
    s,e=i
    if e-s <= d:
        roadlength.append(i)

roadlength.sort(key=lambda x: x[1])

answer=0
q=[]
for i in roadlength:
    if not q:
        heapq.heappush(q,i)
    else:
        while q[0][0]<i[1]-d:
            heapq.heappop(q)
            if not q:
                break
        heapq.heappush(q,i)
    answer=max(answer,len(q))

print(answer)