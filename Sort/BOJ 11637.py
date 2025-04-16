t=int(input())
for _ in range(t):
    n=int(input())
    data=list([int(input()),i] for i in range(1,n+1))
    data.sort(reverse=True)
    tot=sum(i[0] for i in data)
    if data[0][0]==data[1][0]:
        print("no winner")
    elif data[0][0]*2>tot:
        print("majority winner",data[0][1])
    else:
        print("minority winner",data[0][1])