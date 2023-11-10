from collections import deque
n,m=map(int,input().split())
data=deque(sorted(list(map(int,input().split()))))
answer=0
while len(data)>=2:
    a=data.popleft()
    b=data.pop()
    if a+b>=m:
        answer+=1
    else:
        data.append(b)

print(answer)