import heapq
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,d,c=map(int,input().split())
    count=1
    time=0
    virusinfo=[[] for _ in range(n+1)]
    for _ in range(d):
        end,start,val=map(int,input().split())
        virusinfo[start].append([val,end])
    dp=[1e10 for _ in range(n+1)]
    dp[c]=0
    heap=[]
    heapq.heappush(heap,[0,c])
    while heap:
        val,origin=heapq.heappop(heap)
        for tempval,tempcoord in virusinfo[origin]:
            temp=tempval+val
            if temp<dp[tempcoord]:
                if dp[tempcoord]==1e10:
                    count+=1
                dp[tempcoord]=temp
                heapq.heappush(heap,[temp,tempcoord])
    for i in dp:
        if i!=1e10:
            time=max(time,i)
    print(count, time)