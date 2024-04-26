t=int(input())
for i in range(1,t+1):
    a,b=input().split()
    b=str(int(b))    
    print(a, end=" ")
    if max(list(b))>='8':
        print(0,end=" ")
    else:
        print(int(b,8),end=" ")
    print(b,end=" ")
    print(int(b,16))