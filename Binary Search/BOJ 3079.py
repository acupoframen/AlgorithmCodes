n,m=map(int,input().split())
data=list()
for _ in range(n):
    data.append(int(input()))
data.sort()
left=1
right=int(1e18)
while left<=right:
    mid=(left+right)//2
    people=0
    for i in range(n):
        people+=mid//data[i]
    if people<m:
        left=mid+1
    else:
        right=mid-1
print(left)