n,r=map(int,input().split())
mod=1000000007

def power(a,n):
    if n==0:
        return 1
    half=power(a,n//2)
    if n%2:
        return (half*half%mod)*a%mod
    else:
        return half*half%mod

def moduloReverse(i):
    return power(i,mod-2)

def comb(n,r):
    temp=1
    for i in range(r):
        temp=temp*(n-i)%mod
    for i in range(r,0,-1):
        temp=temp*moduloReverse(i)%mod
    return temp

print(comb(n,r))