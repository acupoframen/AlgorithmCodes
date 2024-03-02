n,m=map(int,input().split())
data=list(map(int,input().split()))
start=max(data)
end=sum(data)
while start<=end:
    mid=(start+end)//2
    temp=0
    index=0
    tempgroup=[]
    while index<n:
        subsum=0
        subcount=0
        while index<n and subsum+data[index]<=mid:
            subsum+=data[index]
            subcount+=1
            index+=1
            if m-temp==n-index+1:
                break
        temp+=1
        tempgroup.append(subcount)
    if temp<=m:
        end-=1
    else:
        start+=1
print(mid)
print(*tempgroup)