from collections import deque
n=int(input())
data=deque()
for i in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
answer=0
current=[]
while data:
    a,b=data.popleft()
    while current and current[-1]>b:
        current.pop()
        answer+=1
    if current and current[-1]==b:
        continue
    current.append(b)

while current:
    if current[-1]>0:
        answer+=1
    current.pop()
print(answer)