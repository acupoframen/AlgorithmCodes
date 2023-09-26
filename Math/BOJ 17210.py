n=int(input())
if n>5:
    print("Love is open door")
    exit(0)
a=int(input())
if a==0:
    a=1

else:
    a=0
for i in range(1,n):
    if a==0:
        print(0)
        a=1
    else:
        print(1)
        a=0
