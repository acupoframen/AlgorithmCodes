n=int(input())
data=list(map(int,input().split()))
sums=list(0 for _ in range(n))
sums[0]=data[0]
sums[1]=data[1]
for i in range(2,n):
    sums[i]=sums[i-2]+data[i]

answer=sums[n-2]
for i in range(n-1):
    if i%2:
        if i==1:
            answer=max(answer,sums[i-1]+(sums[n-3]))
        else:
            answer=max(answer,sums[i-1]+sums[n-3]-sums[i-2])
    else:
        if i==0:
            answer=max(answer,sums[i-1])
        else:
            answer=max(answer,data[-1]+sums[i-2]+(sums[n-3]-sums[i-1]))
        
    

print(answer)