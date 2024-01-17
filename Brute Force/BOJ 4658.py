import sys
from itertools import permutations
input=sys.stdin.readline

def change(data):
    data=[data[2]]+data[0:2]
    return data
def calc(data):
    answer=-1
    for i in list(permutations(data,6)):
        i=list(map(list,i))
        for i0 in range(3):
            for i1 in range(3):
                for i2 in range(3):
                    for i3 in range(3):
                        for i4 in range(3):
                            for i5 in range(3):
                                if i[0][0]==i[1][1] and i[1][0]==i[2][1] and i[2][0]==i[3][1] and i[3][0]==i[4][1] and i[4][0]==i[5][1] and i[5][0]==i[0][1]:
                                    temp=0
                                    for k in range(6):
                                        temp+=i[k][2]
                                    answer=max(temp,answer)
                                i[5]=change(i[5])
                            i[4]=change(i[4])
                        i[3]=change(i[3])
                    i[2]=change(i[2])
                i[1]=change(i[1])
            i[0]=change(i[0])                                    
    if answer>=0:
        print(answer)
    else:
        print("none")
data=[]
while True:
    a=input().strip()
    if a=='*':
        calc(data)
        data=[]
    elif a=="$":
        calc(data)
        exit(0)
    else:
        data.append(list(map(int,a.split())))
