a=list(map(int,list(input())))
a.sort()
if a[0]!=0:
    print(-1)
    exit(0)
if sum(a)%3!=0:
    print(-1)
    exit(0)

print(*(sorted(a[1:],reverse=True)),0, sep="")