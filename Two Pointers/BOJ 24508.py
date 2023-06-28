from collections import deque
n,k,t=map(int,input().split())
data=list(map(int,input().split()))
data.sort(reverse=True)
global lim
lim= n-1
for i in range(n):
    if data[i]==0:
        lim=i-1
        break
count=0
data=deque(data[:lim+1])
while True:
    if count>t:
        print("NO")
        break
    if len(data)==1:
        print("NO")
        break
    if len(data)==0:
        print("YES")
        break
    a=data.popleft()
    b=data.pop()
    if k-a==b:
        count+=b
    elif k-a>b:
        count+=b
        a+=b
        data.appendleft(a)
    else:
        count+=k-a
        b=b-k+a
        data.append(b)
