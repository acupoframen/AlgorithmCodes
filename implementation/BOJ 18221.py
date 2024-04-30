import sys
input=sys.stdin.readline
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))

prof=0
seonggyu=0
for i in range(n):
    for j in range(n):
        if data[i][j]==2:
            seonggyu=[i,j]
        elif data[i][j]==5:
            prof=[i,j]
    if prof and seonggyu:
        break


if (prof[0]-seonggyu[0])**2 + (prof[1]-seonggyu[1])**2>=25:
    temp=0
    for i in range(min(prof[0],seonggyu[0]),max(prof[0],seonggyu[0])+1):
        for j in range(min(prof[1],seonggyu[1]),max(prof[1],seonggyu[1])+1):
            if data[i][j]==1:
                temp+=1
    if temp>=3:
        print(1)
    else:
        print(0)
else:
    print(0)