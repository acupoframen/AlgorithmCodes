n,t=map(int,input().split())
if t==1:
    print(1)
    exit(0)

if n==2:
    if t%2==0:
        print(2)
    else:
        print(1)

    exit(0)

value=t%(4*n-2)
if value==0:
    print(2)
elif value>2*n:
    print(4*n-value)
else:
    print(value)