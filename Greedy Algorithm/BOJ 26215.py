n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
time=0
while time<=1440:
    data.sort(reverse=True)
    if len(data)>=2:
        time+=1
        data[0]-=1
        data[1]-=1
        if data[1]==0:
            del data[1]
        if data[0]==0:
            del data[0]
    elif len(data)==1:
        time+=1
        data[0]-=1
        if data[0]==0:
            del data[0]
    else:
        print(time)
        break
    
if time==1441:
    print(-1)
