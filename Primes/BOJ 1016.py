import math
n=10**6+10**3
a=[False,False]+[True]*(n)
for i in range(2,10**3+1):
    if a[i]:
        for j in range(2*i,n+1,i):
            a[j]=False
primeSquared=[i**2 for i in range(2,n) if a[i]]
minNum,maxNum=map(int,input().split())
answer=0
b=[False]*(maxNum+1-minNum)

def calc():
    for i in primeSquared:
        j=math.ceil(minNum/i)
        while i*j<=maxNum:
            b[i*j-minNum]=True
            j+=1

calc()
print(b.count(False))
