import math
n=int(input())
sieve=[1 for _ in range(2000000)]
sieve[0]=0
sieve[1]=0
for i in range(2,int(math.sqrt(2000000))+1):
    if sieve[i]:
        for j in range(2*i,2000000,i):
            sieve[j]=0
while True:
    if sieve[n] and str(n)==str(n)[::-1]:
        print(n)
        break
    n+=1