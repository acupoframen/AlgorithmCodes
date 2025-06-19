import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=list(map(int,input().split()))
r=max(data)
l=0
answer=r

def f(val):
    global answer
    low=data[0]
    high=data[0]
    d=1
    for i in data:
        if high<i:
            high=i
        if low>i:
            low=i
        if high-low>val:
            d+=1
            low=i
            high=i
    return d<=m

while l<=r:
    mid=(l+r)//2
    if f(mid):
        r=mid-1
        answer=min(answer,mid)
    else:
        l=mid+1
print(answer)