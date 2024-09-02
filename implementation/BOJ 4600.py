from collections import deque
while 1:
    b,p=map(int,input().split())
    if (b,p)==(0,0):
        break
    b*=-1
    data=[]
    for _ in range(b):
        c,t=map(int,input().split())
        data.append([c,t,0,0]) #people, time, remaining time, how many ppl
    people=[0 for _ in range(b+1)]
    people[0]=p
    second=0
    while True:
        for i in range(b):
            if people[i]==0:
                continue
            else:
                if data[i][2]>0:
                    continue
                data[i][2]=data[i][1]
                data[i][3]=min(data[i][0],people[i])
                people[i]-=data[i][3]
        for i in range(b):
            if data[i][2]>0:
                data[i][2]-=1

                if data[i][2]==0:
                    people[i+1]+=data[i][3]
                    data[i][3]=0
        if people[-1]==p:
            break
        second+=1
    print(second+1)