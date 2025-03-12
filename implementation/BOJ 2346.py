from collections import deque
n=int(input())
data=deque()
temp=list(map(int,input().split()))
for i in range(1,n+1):
    data.append([i,temp[i-1]])
ball,move=data.popleft()
if move>0:
    move-=1
print(ball,end=" ")
while data:
    while move!=0:
        if move>0:
            temp=data.popleft()
            data.append(temp)
            move-=1
        else:
            temp=data.pop()
            data.appendleft(temp)
            move+=1
    ball,move=data.popleft()
    print(ball,end=" ")
    if move>0:
        move-=1
    