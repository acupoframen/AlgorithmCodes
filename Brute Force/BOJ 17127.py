n=int(input())
data=list(map(int,input().split()))
answer=0
a=1
for i in range(0,n-3):
    a*=data[i]
    b=1
    for j in range(i+1,n-2):
        b*=data[j]
        c=1
        for k in range(j+1,n-1):
            c*=data[k]
            d=1
            for t in range(k+1,n):
                temp=0
                d*=data[t]
            answer=max(answer,a+b+c+d)
print(answer)