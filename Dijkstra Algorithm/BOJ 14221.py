import sys
input=sys.stdin.readline
import heapq
n,m=map(int,input().split())
lines=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    lines[a].append([b,c])
    lines[b].append([a,c])
a,b=map(int,input().split())
purpose=[0]*(n+1)
temp=list(map(int,input().split()))
for i in temp:
    purpose[i]=1 #HOUSE
temp=list(map(int,input().split()))
for i in temp:
    purpose[i]=2 #CVS
answer=[1e10]*(n+1)
values=[1e10]*(n+1)
for i in range(1,n+1):
    if purpose[i]!=1:
        continue
    q=[]
    heapq.heappush(q,[0,i])
    while q:
        value,coordinate=heapq.heappop(q)
        if purpose[coordinate]==2:
            answer[i]=min(answer[i],value)
            continue
        if values[coordinate]<value:
            continue
        for j in lines[coordinate]:
            newCoordinate,newDistance=j
            d=newDistance+value
            if values[newCoordinate]>d:
                values[newCoordinate]=d
                heapq.heappush(q,[d,newCoordinate])

realAnswer=1e10
printout=0
for i in range(1,n+1):
    if purpose[i]==1:
        if realAnswer>answer[i]:
            realAnswer=answer[i]
            printout=i

print(printout)