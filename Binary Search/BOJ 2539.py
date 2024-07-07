n,m=map(int,input().split())
paper=int(input())
wrong=int(input())
data=list()
maxHeight=0
for _ in range(wrong):
    x,y=map(int,input().split())
    maxHeight=max(maxHeight,x)
    data.append([y,x])
data.sort()

left=maxHeight
right=int(1e6)+1
answer=0
while left<=right:
    mid=(left+right)//2
    start=data[0][0]
    count=1
    for y,x in data:
        if y>=start+mid:
            start=y
            count+=1
    if count<=paper:
        right=mid-1
    else:
        left=mid+1
print(left)