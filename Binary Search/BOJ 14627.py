import sys
input=sys.stdin.readline
s,c=map(int,input().split())
data=list(int(input()) for _ in range(s))
minval,maxval=0,1000000000
answer=0
midsave=0
while minval<=maxval:
    count=0
    mid=(minval+maxval)//2
    if mid==0:
        midsave=0
        break
    for i in (data):
        count+=(i//mid)
    if count<c:
        maxval=mid-1
    else:
        if midsave<mid:
            midsave=mid
        minval=mid+1
if midsave==0:
    print(0)
    exit(0)
pacount=0
for i in range(len(data)):
    temp=(data[i]//midsave)
    data[i]-=temp*midsave
    pacount+=temp
print(sum(data)+(pacount-c)*midsave)