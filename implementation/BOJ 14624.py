n=int(input())
if not n%2:
    print("I LOVE CBNU")
    exit(0)
print("*"*n)
print(" "*(n//2),"*",sep="")
for i in range(n//2):
    print(" "*(n//2-i-1),end="")
    print("*",end="")
    print(" "*(i*2+1),end="")
    print("*")