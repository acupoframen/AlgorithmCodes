t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    answer=0
    data=[]
    for _ in range(n):
        data.append(list(map(int,input().split())))
    couponcount=[0]+list(map(int,input().split()))
    for i in range(n):
        cp=data[i][1:-1]
        temp=1e10
        for j in cp:
            temp=min(temp,couponcount[j])
        answer+=temp*data[i][-1]
    print(answer)
