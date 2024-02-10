import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(int(1e4))
n=int(input())
data=list([] for i in range(n+1))
cycleyes=list(0 for i in range(n+1))
visited=[0 for _ in range(n+1)]
answer=[0 for _ in range(n+1)]

def cycle(start,now,count):
    global cycleyes1
    visited[now]=1
    if start==now and count>=2:
        cycleyes1=1
        return
    for i in data[now]:
        if not visited[i]:
            cycle(start,i,count+1)
        elif i==start and count>=2:
            cycle(start,i,count)
    return 

def dist():
    q=deque()
    visited=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if cycleyes[i]:
            q.append(i)
            visited[i]=1
    while q:
        now=q.popleft()
        for i in data[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=1
                answer[i]=answer[now]+1

for _ in range(n):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(1,n+1):
    visited=[0 for _ in range(n+1)]
    cycleyes1=0
    cycle(i,i,0)
    cycleyes[i]=cycleyes1
dist()
print(*answer[1:])

