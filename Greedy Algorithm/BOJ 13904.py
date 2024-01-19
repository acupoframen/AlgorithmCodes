import heapq
q=[]
n=int(input())

for _ in range( n):
    d,w=map(int,input().split())
    heapq.heappush(q,(-w,d))

data=[-1 for _ in range(1001)]
answer=0
while q:
    w,d=heapq.heappop(q)
    for i in range(d,0,-1):
        if data[i]==-1:
            data[i]=-w
            break

for i in data:
    if i!=-1:
        answer+=i

print(answer)