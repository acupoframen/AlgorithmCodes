t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    
    a=min(a,b)
    
    for i in range(n):
        div=a%2
        a//=2
        if div!=0:
            break
    print(n-i)