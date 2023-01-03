n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
low=0
high=data[-1]
answer=0
while low<=high:
    mid=(low+high)//2
    num=0
    for i in range(len(data)):
        if mid<data[i]:
            num+=(data[i]-mid)
    if num<m:
        high=mid-1
    else:
        answer=mid
        low=mid+1
print(answer)