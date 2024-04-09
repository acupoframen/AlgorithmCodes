from math import floor
sieve=[1 for _ in range(1300000)]
sieve[1]=0
for i in range(2,floor(1300000**0.5)+1):
    if sieve[i]:
        for j in range(2*i,1300000,i):
            sieve[j]=0
t=int(input())
for _ in range(t):
    n=int(input())
    if sieve[n]:
        print(0)
    else:
        answer=1
        temp=n
        while not sieve[temp-1]:
            answer+=1
            temp-=1
        temp=n
        while not sieve[temp+1]:
            answer+=1
            temp+=1
        print(answer+1)
