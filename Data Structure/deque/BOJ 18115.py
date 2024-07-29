from collections import deque
n=int(input())
data=list(map(int,input().split()))[::-1]
answer=deque()
for i in range(n):
    if data[i]==1:
        answer.appendleft(i+1)
    elif data[i]==2:
        temp=answer.popleft()
        answer.appendleft(i+1)
        answer.appendleft(temp)
    else:
        answer.append(i+1)

print(*answer)