from collections import deque
n=int(input())
q=deque()
for i in range(10):
    q.append(i)
answer=[]
while q:
    num=q.popleft()
    answer.append(num)
    for i in range(num%10):
        q.append(num*10+i)
answer.sort()
if n>=len(answer):
    print(-1)
else:
    print(answer[n])