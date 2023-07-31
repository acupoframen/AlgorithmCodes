from collections import deque
data=[1e10 for _ in range(200001)]
n,m=map(int,input().split())
data[n]=0
q=deque()
q.append(n)
if n==m:
    print(0)
    exit(0)
while q:
    temp=q.popleft()
    temp1=temp
    while 1<=temp<=200000:
        if data[temp]>data[temp1]:
            q.append(temp)
            data[temp]=data[temp1]
            if temp==m:
                print(data[m])
                exit(0)
        temp*=2
    if temp1!=0 and data[temp1-1]>data[temp1]+1:
        q.append(temp1-1)
        data[temp1-1]=data[temp1]+1
        if temp1-1==m:
            print(data[m])
            exit(0)    
    if temp1<=199999 and data[temp1+1]>data[temp1]+1:
        q.append(temp1+1)
        data[temp1+1]=data[temp1]+1
        if temp1+1==m:
            print(data[m])
            exit(0)
    
    