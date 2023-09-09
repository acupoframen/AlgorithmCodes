import sys
input=sys.stdin.readline

t=int(input())
data=[1e10 for _ in range(100001)]
data[0]=0
data[1]=1
for i in range(2,100001):
    data[i]=data[i-1]+data[i-2]

for _ in range(t):
    num=int(input())
    if num==1:
        print(2)
        continue
    left=0
    right=100000
    mid=0
    while left<=right:
        mid=(left+right)//2
        if data[mid]>num:
            right=mid-1
        elif data[mid]==num:
            print(mid)
            break
        else:
            left=mid+1