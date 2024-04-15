from collections import deque
a,b,n,m=map(int,input().split())

q=deque()
q.append(n)
data=[1e10 for _ in range(100001)]
data[n]=0
def calc(ori,num):
    if 0<=num<=100000 and data[num]==1e10:
        data[num]=ori+1
        q.append(num)
while q:
    num=q.popleft()
    if num==m:
        print(data[num])
        break
    ori=data[num]
    
    calc(ori,num+1)
    calc(ori,num-1)
    calc(ori,num+a)
    calc(ori,num+b)
    calc(ori,num-a)
    calc(ori,num-b)
    calc(ori,num*a)
    calc(ori,num*b)