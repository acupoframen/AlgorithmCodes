n,k=map(int,input().split())
data=list(map(int,input().split()))
for i in range(k):
    num=data[i]*100//n
    if 0<=num<=4:
        print(1, end=" ")
    elif 4<num<=11:
        print(2, end=" ")
    elif 11<num<=23:
        print(3, end=" ")
    elif 23<num<=40:
        print(4, end=" ")
    elif 40<num<=60:
        print(5, end=" ")
    elif 60<num<=77:
        print(6, end=" ")
    elif 77<num<=89:
        print(7, end=" ")
    elif 89<num<=96:
        print(8, end=" ")
    else:
        print(9, end=" ")