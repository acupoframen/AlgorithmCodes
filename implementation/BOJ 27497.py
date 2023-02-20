from collections import deque
n=int(input())
answer=deque()
recent=list()
for _ in range(n):
    data=list(input().split())
    if data[0]=='1':
        answer.append(data[1])
        recent.append(1)
    elif data[0]=='2':
        answer.appendleft(data[1])
        recent.append(-1)
    else:
        if recent!=[]:
            cal=recent.pop()
            if cal==1:
                answer.pop()
            else:
                answer.popleft()
if len(answer)==0:
    print("0")
    exit(0)
for i in answer:
    print(i,end="")