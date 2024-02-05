hi=int(input())
data=list(0 for _ in range(1001))
for i in range(1,100):
    data[i]=1
for i in range(101,1001):
    n=str(i)
    if int(n[0])+int(n[2])==2*int(n[1]):
        data[i]=1

print(sum(data[1:hi+1]))