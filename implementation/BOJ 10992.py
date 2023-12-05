n=int(input())
print(" "*(n-1),end=""); print("*")
if n==1:
    exit(0)
for i in range(2,n):
    temp=i*2-2
    print(" "*(n-i), end="")
    print("*",end="")
    print(" "*(temp-1),end="")
    print("*")
print("*"*(2*n-1))
