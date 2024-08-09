t=int(input())
for _ in range(t):
    n=int(input())
    data=[]
    idx=0
    while n:
        if n%2==1:
            data.append(idx)
        idx+=1
        n//=2
    print(*data)