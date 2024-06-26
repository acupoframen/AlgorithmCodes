n,k=map(int,input().split())
data=[0 for _ in range(1000001)]

for _ in range(n):
    s,e=map(int,input().split())
    for i in range(s,e):
        data[i]+=1
l,r,temp=0,0,0
while 0<=l<=r and r<int(1e6)+1:
    if temp==k:
        print(l,r)
        exit(0)
    elif temp<k:
        temp+=data[r]
        r+=1
    else:
        temp-=data[l]
        l+=1
print(0,0)