t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    answer=0
    maxval=data[-1]
    for j in range(n-2,-1,-1):
        if data[j]<=maxval:
            answer+=maxval-data[j]
        else:
            maxval=data[j]
    print(answer)