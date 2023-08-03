n=int(input())
data=list(map(int,input().split()))
data.sort()

temp=1e10
answer=[1e10,1e10,1e10]
for i in range(n):
    l,r=i+1,n-1
    while l<r:
        if temp>abs(data[i]+data[l]+data[r]):
            answer=[data[i],data[l],data[r]]
            temp=abs(sum(answer))
        if not data[i]+data[l]+data[r]:
            print(data[i],data[l],data[r])
            exit(0)
        elif data[i]+data[l]+data[r]>0:
            r-=1
        else:
            l+=1

print(*answer)