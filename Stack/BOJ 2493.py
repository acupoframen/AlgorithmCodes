from collections import deque
n=int(input())
data=[0]+list(map(int,input().split()))
answer=[]
q=deque()
for i in range(1,n+1):
    while q:
        if q[-1][1] > data[i]:
            answer.append(q[-1][0])
            break
        else:
            q.pop()
    if not q:
        answer.append(0)
    q.append([i,data[i]])

print(*answer)