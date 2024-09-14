import sys
input=sys.stdin.readline
data=[]
n,m=map(int,input().split())
for _ in range(n):
    start,end=map(int,input().split())
    if start>end:
        data.append([end,start])

data.sort(key= lambda x: -x[1])
temp=[]
if not data:
    print(m)
    exit(0)
tempstart, tempend= data[0]
for i in range(1,len(data)):
    start,end=data[i]
    if tempstart<=end:
        tempstart=min(tempstart,start)
    else:
        temp.append([tempstart,tempend])
        tempstart,tempend=start,end
temp.append([tempstart,tempend])
answer=m
for i in range(len(temp)):
    answer+= 2*(temp[i][1]-temp[i][0])
print(answer)