a,b=input().split()
originalnumber=a
a=b+a
a=int(a)
sieve=[0,0]+[0]*(10000001)
for i in range(2,int(a**0.5)+1):
    if sieve[i]==0:
        for j in range(2*i,a+1,i):
            sieve[j]=1

if not sieve[int(originalnumber)] and not sieve[a]:
    print("Yes")
else:
    print("No")