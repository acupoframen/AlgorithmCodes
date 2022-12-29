'''t=int(input())
data=[]
for _ in range(t):
    data.append(list(map(int,input().split())))
num=0
primes=[]
for i in data:
    num=max(sum(i),num)
a=[False,False]+[True]*(num-1)
for i in range(2,int(num**0.5)+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,num+1,i):
            a[j]=False
for i in range(len(a)):
    if a[i]:
        primes.append(i)
for i in data:
    limit=sum(i)
    flag=0
    for j in range(2,limit//2+1):
        if j in primes and limit-j in primes:
            flag=1
            print("YES")
            break
    if not flag:
        print("NO")'''
#==============================

n=2*(10**6)
a=[False,False]+[True]*(n-1)
for i in range(2,int(n**0.5)+1):
    if a[i]:
        for j in range(2*i,n+1,i):
            a[j]=False
prime=[i for i in range(2,n) if a[i]]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a+b<4:
        print("NO")
    elif not (a+b)%2:
        print("YES")
    else:
        if a+b-2>=n:
            flag=0
            for p in prime:
                if not (a+b-2)%p:
                    flag=1
                    print("NO")
                    break
            if not flag:
                print("YES")
        else:
            if a+b-2 in prime:
                print("YES")
            else:
                print("NO")
