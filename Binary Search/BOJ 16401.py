m,n=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
left=1
right=1e10
while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in range(n):
        cnt+=data[i]//mid
    if cnt>=m:
        left=mid+1
    else:
        right=mid-1
print(int(right))