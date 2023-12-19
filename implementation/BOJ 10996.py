n=int(input())
for i in range(n):
    for j in range(2):
        if j%2==1:
            print(" *"*(n//2))
        else:
            print("* "*(n-n//2) )
