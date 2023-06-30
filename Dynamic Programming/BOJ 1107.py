from collections import deque
import heapq
goal=int(input())
n=int(input())
if n!=0:
    broken=list(map(int,input().split()))
    notbroken=[i for i in range(0,10) if i not in broken]
else:
    notbroken=[i for i in range(0,10)]
q=deque()
data=[1e10 for _ in range(0,1000001)]

newq=[]
heapq.heappush(newq,[0,100])
for i in notbroken:
    data[i]=1
    q.append(i)
    heapq.heappush(newq,[1,i])
while q:
    num=q.popleft()
    if num<=1000000:
        for i in notbroken:
            newNum=num*10+i
            if newNum<=1000000 and data[newNum]>data[num]+1:
                data[newNum]=data[num]+1
                q.append(newNum)
                heapq.heappush(newq, [data[num]+1,newNum])
data[100]=0
while True:
    value,num=heapq.heappop(newq)

    if num>1000000:
        continue
    if num==goal:
        print(data[num])
        break
    if num<=999999 and data[num+1]>data[num]+1:
        data[num+1]=data[num]+1
        heapq.heappush(newq,[data[num]+1,num+1])
    if num-1>=0 and data[num-1]>data[num]+1:
        data[num-1]=data[num]+1
        heapq.heappush(newq,[data[num]+1,num-1])
    
    