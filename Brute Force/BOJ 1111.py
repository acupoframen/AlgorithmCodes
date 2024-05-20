from collections import deque
n=int(input())
data=list(map(int,input().split()))
if n==1 or (n==2 and data[0]!=data[1]):
    print("A")
    exit(0)
elif data[0]==data[1]:
    a=0
    b=data[0]
else:
    a=(data[2]-data[1])/(data[1]-data[0])
    b = data[1] - data[0]*a
    if int(a)!=a or int(b)!=b:
        print("B")
        exit(0)
i = 1
while i<n-1:
    if data[i]*a+b==data[i+1]:
        i+=1
    else:
        print("B")
        exit(0)
print(int(a*int(data[-1])+b))