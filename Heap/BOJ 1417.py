import heapq
n=int(input())
dasom=int(input())
q=[]
for i in range(n-1):
    num=int(input())
    heapq.heappush(q,-num)
if n==1:
    print(0)
    exit(0)
answer=0
while q:
    num=heapq.heappop(q)
    num*=-1
    if num<dasom:
        print(answer)
        break
    num-=1
    answer+=1
    dasom+=1
    heapq.heappush(q,-num)