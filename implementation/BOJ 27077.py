from copy import deepcopy
data=[[i] for i in range(4)]
for i in range(4):
    temp=list(map(int,input().split()))
    for j in temp:
        data[i].append(j)
    data[i][3]+=1

n=int(input())
kp=0 #korea>portugal : > 
ug=0 # uruguay?ghana : >

def f():
    temp=deepcopy(data)
    temp.sort(key=lambda x: (-x[3],-(x[1]-x[2]),-x[1],-x[0]))

    if not temp[0][0] or not temp[1][0]:
        print("cry")
    else:
        print("unhappy")

f()
for _ in range(n):
    team=input()
    if team=="korea":
        kp+=1
        data[0][1]+=1
        data[3][2]+=1
        if kp==0:
            data[0][3]+=1
            data[3][3]-=2
        elif kp==1:
            data[0][3]+=2
            data[3][3]-=1
    elif team=='portugal':
        kp-=1
        data[3][1]+=1
        data[0][2]+=1
        if kp==0:
            data[3][3]+=1
            data[0][3]-=2
        elif kp==-1:
            data[3][3]+=2
            data[0][3]-=1
    elif team=='uruguay':
        ug+=1
        data[1][1]+=1
        data[2][2]+=1
        if ug==0:
            data[1][3]+=1
            data[2][3]-=2
        elif ug==1:
            data[1][3]+=2
            data[2][3]-=1
    else:
        ug-=1
        data[2][1]+=1
        data[1][2]+=1
        if ug==0:
            data[2][3]+=1
            data[1][3]-=2
        elif ug==-1:
            data[2][3]+=2
            data[1][3]-=1
    f()