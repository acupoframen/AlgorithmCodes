n=5*10**6
a=[False,False]+[True]*(n-1)
for i in range(2,n+1):
    if a[i]:
        for j in range(2*i,n+1,i):
            a[j]=False
primes=[]
for i in range(n):
    if a[i]:
        primes.append(i)

n=int(input() )
l,r=0,0
answer=0
while n>=primes[r]:
    sumNum=sum(primes[l:r+1])
    if sumNum>n:
        l+=1
    elif sumNum<n:
        r+=1
    else:
        answer+=1
        l+=1

print(answer)
