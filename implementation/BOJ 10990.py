n=int(input())
for i in range(n):
    if i!=0:
        print(" "*(n-i-1),end="")
        print("*",end="")
    else:
        print(" "*(n-i-1),end="")
        print("*")
    if i!=0:
        print(" "*(2*i-1),end="")
        print("*")

