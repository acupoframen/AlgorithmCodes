t=int(input())
for _ in range(t):
    data=list(map(int,input().split()))
    d=((data[0]-data[3])**2+(data[1]-data[4])**2)**0.5
    if data[4]==data[5]==0:
        print (0)
    elif not d:
        if data[2]==data[5]:
            print(-1)
        else:
            print(0)
    else:
        if d==data[2]+data[5] or d==abs(data[2]-data[5]):
            print(1)
        elif data[2]+data[5]>d>abs(data[2]-data[5]):
            print(2)
        else:
            print(0)