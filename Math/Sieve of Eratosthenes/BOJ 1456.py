import math
a,b=map(int,input().split())

data=[1 for _ in range(int(1e7)+1)]
data[0]=0
data[1]=0
for i in range(2,int(1e7)+1):
    if data[i]:
        for j in range(i*2,int(1e7)+1,i):
            data[j]=0

count=0
for i in range(2,int(1e7)+1):
    if data[i]:
        curr=i**2
        while curr<=b:
            if a<=curr:
                count+=1
            curr*=i
print(count)