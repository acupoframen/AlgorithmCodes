from collections import defaultdict
import sys
import math
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
endpoints=list(list(map(int,input().split())) for _ in range(m))
d=defaultdict(list)
for i in range(n):
    x,y=data[i]
    if x==0:
        d[(int(1e10),int(1e10))].append(y)
    else:
        d[(x//math.gcd(x,y),y//math.gcd(x,y))].append(x)
answer=0
for i in d.keys():
    d[i].sort()
for i in range(m):
    x,y=endpoints[i]
    if x==0:
        cx=int(1e10)
        cy=int(1e10)
    else:
        cx,cy=x//math.gcd(x,y),y//math.gcd(x,y)
    if x==0:
        var=y
    else:
        var=x
    if d[(cx,cy)]:
        left=0
        right=len(d[(cx,cy)])-1
    else:
        continue
    temp=0
    while left<=right:
        mid=(left+right)//2
        if d[(cx,cy)][mid]>=0:
            right=mid-1
        else:
            left=mid+1
    if var>0:
        temp=left
    else:
        temp=right
    left=0
    right=len(d[(cx,cy)])-1
    if var>0:
        while left<=right: 
            mid=(left+right)//2
            if d[(cx,cy)][mid]<=var:
                left=mid+1
            else:
                right=mid-1
        temp=right-temp+1
    else:
        while left<=right:
            mid=(left+right)//2
            if var<=d[(cx,cy)][mid]:
                right=mid-1
            else:
                left=mid+1
        temp=temp-left+1
    answer=max(answer,temp)
print(answer)