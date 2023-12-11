t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    data=0
    for _ in range(n):
        a,b=input().split()
        data+=int(a)*float(b)
        count+=int(a)
    print(count,data/count)