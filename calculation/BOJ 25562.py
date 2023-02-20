n=int(input())
print(n*(n-1)//2)
for i in range(n):
    print(2**i, end=' ')
print()
print(n-1)
for i in range(1,n+1):
    print(i,end=' ')
