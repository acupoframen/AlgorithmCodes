n,m,k=map(int,input().split())
currPos=k-3
currPos+=n*100000
currPos%=n
if not (currPos+m)%n:
    print(n)
else:
    print((currPos+m)%n)