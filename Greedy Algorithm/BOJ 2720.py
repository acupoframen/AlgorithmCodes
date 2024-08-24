t=int(input())
for _ in range(t):
    n=int(input())
    q=0
    ni=0
    d=0
    while n>=25:
        q+=1
        n-=25
    while n>=10:
        ni+=1
        n-=10
    while n>=5:
        d+=1
        n-=5
    print(q,ni,d,n)