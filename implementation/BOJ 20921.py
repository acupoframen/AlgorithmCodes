from collections import deque
n,k=map(int,input().split())
data=list(i for i in range(1,n+1))
templen=n-1
answer=[]
while True:
    if k<=templen:
        data=data[:templen-k]+list(data[-1:])+data[templen-k:-1]
        print(*answer, *data)
        break
    answer.append(data[-1])
    data=data[:-1]
    k-=templen
    templen-=1
