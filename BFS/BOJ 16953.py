from collections import deque
a,b=map(int,input().split())
q=deque()
q.append([a,0])
while q:
    num,val=q.popleft()
    if 2*num==b:
        print(val+2)
        exit(0)
    if 2*num<b:
        q.append([2*num,val+1])
    if 10*num+1==b:
        print(val+2)
        exit(0)
    if 10*num+1<b:
        q.append([10*num+1,val+1])

print(-1)