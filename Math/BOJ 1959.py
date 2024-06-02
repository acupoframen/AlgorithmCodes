m,n=map(int,input().split())
if m>n:
    print(2*(n-1)+1)
else:
    print(2*(m-1))
if m==n:
    if m%2:
        print((m-1)//2+1,(m-1)//2+1)
    else:
        print(m//2+1,m//2)
elif m>n:
    if n%2:
        print(n//2+1+(m-n),n//2+1)
    else:
        print(n//2+1,n//2)
else:
    if m%2:
        print(m//2+1,m//2+1+(n-m))
    else:
        print(m//2+1,m//2)