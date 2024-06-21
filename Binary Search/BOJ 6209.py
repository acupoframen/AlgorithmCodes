d,n,m=map(int,input().split())
data=[0]+list(int(input()) for _ in range(n))+[d]
data.sort()
left=1
right=1000000000
while left<=right:
    mid=(left+right)//2
    temp=0
    before=data[0]
    for i in range(1,n+2):
        if data[i]-before<=mid:
            temp+=1
        else:
            before=data[i]
    if temp<=m:
        left=mid+1
    else:
        right=mid-1
print(left)