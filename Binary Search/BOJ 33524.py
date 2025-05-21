n,m=map(int,input().split())
difficulty=list(map(int,input().split()))
difficulty.sort()
level=list(map(int,input().split()))

for i in level:
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if difficulty[mid]<=i:
            left=mid+1
        else:
            right=mid-1
    temp=1
    while True:
        if 3*temp*(temp-1)+1 <= left:
            temp+=1
        else:
            break
    print(temp-1,end=" ")