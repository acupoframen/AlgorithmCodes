n=int(input())
dataleft=[]
dataright=[]
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    dataleft.append(a-b)
    dataright.append(a+b)
    data.append([a-b,a+b])
dataleft.sort()
dataright.sort()
for i in range(n):
    a,b=data[i]
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if dataright[mid]>=a:
            right=mid-1
        else:
            left=mid+1
    print(left+1,end=" ")
    a,b=data[i]
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if dataleft[mid]>b:
            right=mid-1
        else:
            left=mid+1
    print(right+1)