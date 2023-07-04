from collections import deque
n=int(input())
data=[[] for _ in range(n)]
inputs=list(map(int,input().split()))
start=0
for i in range(len(inputs)):
    if inputs[i]==-1:
        start=i
    else:
        data[inputs[i]].append(i)

eraseNum=int(input())
answer=0
q=deque([start])
inputs[eraseNum]=[]
for i in range(len(inputs)):
    if eraseNum in data[i]:
        data[i].remove(eraseNum)
while q:
    point=q.popleft()
    if point==eraseNum:
        continue
    if data[point]:
        for i in data[point]:
            q.append(i)
    else:
        answer+=1

if (n==1):
    print(0)
else:
    print(answer)