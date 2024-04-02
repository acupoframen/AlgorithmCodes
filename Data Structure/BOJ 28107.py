from collections import deque
n,m=map(int,input().split())
data=[deque() for _ in range(200001)]
for i in range(1,n+1):
    temp=list(map(int,input().split()))[1:]
    for j in temp:
        data[j].append(i)
answer=[0 for _ in range(n+1)]
sushi=list(map(int,input().split()))
for i in sushi:
    if data[i]:
        answer[data[i].popleft()]+=1

print(*answer[1:])