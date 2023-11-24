x,n=map(int,input().split())
for i in range(n):
    if x%2==0:
        x=6^(x//2)
    else:
        x=6^(2*x)
print(x)