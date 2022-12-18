data=list(map(int,input().split()))
if len(set(data))==1:
    print(10000+data[0]*1000)
elif len(set(data))==2:
    if data[0]==data[1]:
        print(1000+data[0]*100)
    elif data[0]==data[2]:
        print(1000+data[0]*100)
    else:
        print(1000+data[1]*100)
else:
    data.sort(reverse=True)
    print(data[0]*100)
