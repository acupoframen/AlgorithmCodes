n=int(input())
data=[0 for _ in range(1000001)]
data[1]=1
for i in range(2,1000001):
    data[i]=(data[i-2]+data[i-1])%1000000000

if n<0:
    n=-n
    if n%2==0:
        print(-1)
        print(data[n]%1000000000)
    else:
        print(1)
        print(data[n]%1000000000)
elif n==0:
    print(0)
    print(0)
else:
    print(1)
    print(data[n]%1000000000)