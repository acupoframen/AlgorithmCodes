import heapq
n=int(input())
q=[]
for _ in range(n):
    start=0
    time,end=map(int,input().split())
    heapq.heappush(q,[end,time,0])

m=int(input())
q2=[]
for _ in range(m):
    start,time,end=map(int,input().split())
    heapq.heappush(q2,[start,end,time])

current=0
while q:
    print(current,q)
    end,time,start=heapq.heappop(q)
    if q2 and (end>q2[0][2] or (end==q2[0][2] and q2[0][1]<time)):
        newstart,newtime,newend=heapq.heappop(q2)
        heapq.heappush(q,[newend,newtime,newstart])
        heapq.heappush(q,[end,time-(newstart-current),start])
    current=max(current,start)
    if end<current+time:
        print("NO")
        exit(0)
    current+=time-(newstart-current)
while q2:
    temp=heapq.heappop(q2)
    heapq.heappush(q,[temp[1],temp[2],temp[0]])
while q:
    end,time,start=heapq.heappop(q)    
    current=max(current,start)
    if end<current+time:
        print("NO")
        exit(0)
    current+=time
print("YES")
print(current)