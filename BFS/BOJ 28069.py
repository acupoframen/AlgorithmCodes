from collections import deque

n,k=map(int,input().split())

data=[0 for _ in range(n+1)]

q=deque()
q.append([1,1])

while q:
    location, value=q.popleft()
    if data[location]:
        continue
    if value>k:
        print("water")
        exit(0)
    if location==n:
        print("minigimbob")
        exit(0)
    data[location]=1
    if location+1<=n:
        q.append([location+1,value+1])
    if location+location//2<=n:
        q.append([location+location//2,value+1])

print("water")