for _ in range(3):
    data=list(map(int,input().split()))
    if sum(data)==0:
        print("D")
    elif sum(data)==1:
        print("C")
    elif sum(data)==2:
        print("B")
    elif sum(data)==3:
        print("A")
    else:
        print("E")