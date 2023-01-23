n,c=map(int,input().split())
data=[int(input()) for _ in range(n)]
data.sort()
l,r=0,data[-1]-data[0]
res=0
while l<=r:
    mid= (l+r)//2
    curr=0
    answer=1
    for i in range(1,len(data)):
        if data[i]-data[curr]>=mid:
            answer+=1 
            curr=i
    if answer<c:
        r=mid-1
    else:
        res=mid
        l=mid+1

print(res)