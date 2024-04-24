n,m,l=map(int,input().split())

data=list(map(int,input().split()))
data.append(0)
data.append(l)
data.sort()
answer=0
left=1
right=l-1
dist=[]
for i in range(1,len(data)):
    dist.append(data[i]-data[i-1])
while left<=right:
    mid=(left+right)//2 #거리
    temp=0 #주유소 설치 가능 개수
    for i in dist:
        temp+=(i-1)//mid
    if temp<=m: #주유소 적음. 덜 설치 가능.
        right=mid-1
    
    else: #주유소 너무 많이 필요함. 거리를 줄여야함.
        left=mid+1
print(left)