from math import comb
n,m,k=map(int,input().split())
t=comb(n+m,m)
if t>int(1e9) or k<=t:
    k-=1
    while k:
        for i in range(m,-1,-1):
            t=comb(n+i-1,i)
            if t<=k:
                k-=t
                m=i-1
                print("z",end="")
            else:
                break
        print("a",end="")
        n-=1
    print("a"*n,end="")
    print("z"*m,end="")
else:
    print(-1)