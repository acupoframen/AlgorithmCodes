import heapq
n = int(input())  
k = int(input())  
data = []
for i in range(n):
    a,*b=map(int,input().split())
    data.append(b)
q=[]
heapq.heappush(q,[0,0,1]) #tcount, stage, height

dijk=list(list(1e10 for _ in range(21)) for _ in range(n+1))
while q:
    tcount,stage,height=heapq.heappop(q)
    if tcount>k:
        break
    if stage==n:
        print(tcount)
        exit(0)
    for st in data[stage]:
        if tcount>=dijk[stage][st]:
            continue
        if st in [height-1,height,height+1]:
            dijk[stage][st]=tcount
            heapq.heappush(q,[tcount,stage+1,st])
        elif height<10 and height*2==st:
            dijk[stage][st]=tcount
            heapq.heappush(q,[tcount,stage+1,st])
        elif height>=10 and st==20:
            dijk[stage][st]=tcount
            heapq.heappush(q,[tcount,stage+1,st])
        else:
            dijk[stage][st]=tcount+1
            heapq.heappush(q,[tcount+1,stage+1,st])
print(-1)