t=int(input())
for i in range(t):
    n=int(input())
    temp=1
    for i in range(1,n+1):
        temp*=i
        temp%=10
    print(temp)