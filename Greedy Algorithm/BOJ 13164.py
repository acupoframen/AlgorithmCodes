import heapq
n,k=map(int,input().split())
data=list(map(int,input().split()))
q=[]
for i in range(n-1):
    heapq.heappush(q,[-(data[i+1]-data[i]),i])
cuts=[]
for i in range(k-1):
    cuts.append(heapq.heappop(q)[1])
cuts.sort()
temp=0
answer=0
for i in cuts:
    answer+=(data[i]-data[temp])
    temp=i+1
answer+=(data[n-1]-data[temp])
print(answer)