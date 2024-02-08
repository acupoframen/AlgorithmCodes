n,m=map(int,input().split())
a,b=n,m
while a%b:
    a,b=b,a%b
print(m-b)