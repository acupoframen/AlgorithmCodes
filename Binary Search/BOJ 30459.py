n,m,r=map(int,input().split())
loc=list(map(int,input().split()))
length=list(map(int,input().split()))

loc.sort()
locations=[]
answer=-1
for i in range(n-1):
    for j in range(i+1,n):
        locations.append(abs(loc[j]-loc[i]))

locations=list(set(locations))
locations.sort()
for i in range(m):
    left=0
    right=len(locations)-1
    while left<=right:
        mid=(left+right)//2
        if locations[mid]*length[i]<=2*r:
            answer=max(answer,locations[mid]*length[i])
            left=mid+1
        else:
            right=mid-1

if answer!=-1:
    print("%.1f" %(answer/2))
else:
    print(-1)