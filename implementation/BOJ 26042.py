from collections import deque
n=int(input())
answer=[0,1e10]
curr=0
q=deque([])
for _ in range(n):
    a,*b=(map(int,input().split()))
    if a==1:
        q.append(b[0])
        if len(q)>answer[0]:
            answer=[len(q),q[-1]]
        elif len(q)==answer[0]:
            if answer[1]>b[0]:
                answer=[len(q),b[0]]
    else:
        q.popleft()

print(*answer)