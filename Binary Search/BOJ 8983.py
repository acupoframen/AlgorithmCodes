m,n,l=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
answer=0
for _ in range(n):
    x,y=map(int,input().split())
    left=0
    right=m-1
    mid=0
    while left<=right:
        mid=(left+right)//2
        if data[mid]==x:
            right=mid
            break
        elif data[mid]<x:
            left=mid+1
        else:
            right=mid-1
    dist=abs(x-data[right])+y
    if right+1<m:
        dist=min(dist,abs(x-data[right+1])+y)
    if dist<=l:
        answer+=1
print(answer)