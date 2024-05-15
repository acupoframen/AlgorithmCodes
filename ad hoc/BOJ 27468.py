n=int(input())
print("YES")
if n%4==2:
    for i in range(1,n+1):
        if i%4==1:
            print(i+1, end=' ')
        elif i%4==2:
            print(i-1,end=" ")
        elif i%4==3:
            print(i,end=" ")
        else:
            print(i,end=" ")
else:
    for i in range(1,n+1):
        if i%4==1:
            print(i,end=" ")
        elif i%4==2:
            print(i+1,end=" ")
        elif i%4==3:
            print(i-1,end=" ")
        else:
            print(i,end=" ")