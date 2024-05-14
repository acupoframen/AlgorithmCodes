from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    data=list(input().split())
    q=deque()
    for i in data:
        if ''.join(list(q)+[i])>''.join([i]+list(q)):
            q.appendleft(i)
        else:
            q.append(i)
    print("".join(list(q)))