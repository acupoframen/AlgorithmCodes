import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(map(int,input().strip())) for _ in range(n))
answer=0
for i in range(1<<n*m):
    temp=0
    for x in range(n):
        rowtemp=0
        for y in range(m):
            idx=x*m+y
            if i & ( 1<<idx):
                rowtemp=rowtemp*10+data[x][y]
            else:
                temp+=rowtemp
                rowtemp=0
        temp+=rowtemp
    for y in range(m):
        coltemp=0
        for x in range(n):
            idx=x*m+y
            if not i & (1<<idx):
                coltemp=coltemp*10+data[x][y]
            else:
                temp+=coltemp
                coltemp=0
        temp+=coltemp
    answer=max(answer,temp)

print(answer)