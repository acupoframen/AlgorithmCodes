n,k=map(int,input().split())
data=list(int(input()) for _ in range(n))
right=max(data)
left=0
while left<=right:
    temp=0
    mid=(left+right)//2
    if mid==0:
        break
    for i in data:
        if i==0:
            continue
        temp+=i//mid
    if temp>=k:
        left=mid+1
    else:
        right=mid-1
print(right)