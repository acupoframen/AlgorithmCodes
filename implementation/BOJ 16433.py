n,r,c=map(int,input().split())
for i in range(n):
    for j in range(n):
        if (r+c)%2 and (i+j)%2:
            print("v",end="")
        elif (r+c)%2 and (i+j)%2==0:
            print(".",end="")
        elif (r+c)%2==0 and (i+j)%2:
            print(".",end="")
        else:
            print("v",end="")
    print()