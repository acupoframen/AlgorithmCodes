sieve=[0,0]+[1]*int(1e6)
for i in range(2,len(sieve)):
    if sieve[i]:
        for j in range(2*i,len(sieve),i):
            sieve[j]=0

t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(2,min(int(1e6)+1,int(n**0.5)+1)):
        if sieve[i] and not n%i:
            print('NO')
            break
    else:
        print("YES")