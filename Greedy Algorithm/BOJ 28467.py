n=int(input())
data=[1e10]+list(map(int,input().split()))+[1e10]
answer=0
while len(data)!=3:
    temp=0
    minval=1e10
    side=1e10
    lr=0
    for i in range(len(data)):
        if data[i]<minval:
            temp=i
            minval=data[i]
            if data[i-1]<data[i+1]:
                side=data[i-1]
                lr=0
            else:
                side=data[i+1]
                lr=1
        if data[i]==minval:
            if min(data[i-1],data[i+1])<side:
                temp=i
                minval=data[i]
                if data[i-1]<data[i+1]:
                    side=data[i-1]
                    lr=0
                else:
                    side=data[i+1]
                    lr=1
    answer+=(minval+side)
    if lr==0:
        data=data[:temp-1]+[side]+data[temp+1:]
    else:
        data=data[:temp]+[side]+data[temp+2:]
print(answer)