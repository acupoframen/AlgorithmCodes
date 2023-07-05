k,n=map(int,input().split())
data=[]
for _ in range(k):
    data.append(int(input()))
data.sort()
minNum=1
maxNum=max(data)
while minNum<=maxNum:
    num=0
    mid=(minNum+maxNum)//2
    for i in data:
        num+=i//mid
    if num>=n:
        minNum=mid+1
    else:
        maxNum=mid-1
print(maxNum)
