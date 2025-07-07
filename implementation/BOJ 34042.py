n,m=map(int,input().split())
for _ in range(m):
    data=list(map(int,input().split()))
    if n==1:
        print(data[0])
        continue
    if min(data)==max(data)==0:
        print(0)
        continue
    if data.count(0)==n-1:
        print(max(0,max(data)))
        continue
    data.sort(reverse=True)
    smallestneg=0
    
    temp=1
    for i in data:
        if i:
            temp*=i
        if not smallestneg and i<0:
            smallestneg=i
    if temp<0:
        if smallestneg:
            temp//=smallestneg
    
    print(max(data[0],temp))