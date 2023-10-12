from collections import deque
n,m=map(int,input().split())
data=list(map(int,input().split()))
pages=[0 for _ in range(n+1)]+[1 for _ in range(n)]

for i in range(m):
    pages[data[i]]=1
need=[]
for i in range(1,n+1):
    if pages[i]==0:
        need.append(i)
uptowhere=0
answer=0
q=deque(need)
while q:
    a=q.popleft()
    b=a
    while 0 in pages[b+1:b+4]:
        if not q:
            break
        b=q.popleft()
    
    answer+=(b-a+1)*2 +5
print(answer)