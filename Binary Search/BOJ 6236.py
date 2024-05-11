n,m=map(int,input().split())
data=list(int(input()) for _ in range(n))
l=min(data)
r=10000*n
while l<=r:
    mid=(l+r)//2
    num=1
    currentMoney=mid
    for i in range(n):
        if currentMoney<data[i]:
            num+=1
            currentMoney=mid
        currentMoney-=data[i]
    if num>m or mid<max(data):
        l=mid+1
    else:
        r=mid-1

print(l)