n=int(input())
for i in range(n):
    temp=n-i-1
    print(" "*temp, sep="", end="")
    print("*"*(2*i+1),sep="")

for i in range(n-2,-1,-1):
    temp=n-i-1
    print(" "*temp, sep="", end="")
    print("*"*(2*i+1),sep="")