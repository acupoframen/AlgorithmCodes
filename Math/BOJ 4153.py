while(1):
    data=list(map(int,input().split()))
    data.sort()
    if data==[0,0,0]:
        exit(0)
    if data[0]**2+data[1]**2==data[2]**2:
        print('right')
    else:
        print('wrong')