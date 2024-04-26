n,m,p=map(int,input().split())
for i in range(n):
    data=list(map(int,input().split()))
    data.sort()
    minusone=data.count(-1)
    temp=minusone
    for j in data[temp:]:
        if j>p:
            while j>p:
                if minusone>=1:
                    minusone-=1
                    p*=2
                else:
                    print(0)
                    exit(0)
            p+=j
        else:
            p+=j
    while minusone:
        minusone-=1
        p*=2
print(1)