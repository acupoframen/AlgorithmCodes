import sys
from collections import deque
sys.setrecursionlimit(int(1e4))
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    data=list(list() for _ in range(n+1))
    parents=list(0 for _ in range(n+1))
    for i in range(n-1):
        a,b=map(int,input().split())
        data[a].append(b)
        parents[b]=a
    for i in range(1,n+1):
        if parents[i]==0:
            root=i
            break
    a,b=map(int,input().split())
    q=deque()
    q.append(root)
    depth=list(0 for _ in range(n+1))
    while q:
        num=q.popleft()
        for i in data[num]:
            depth[i]=1+depth[num]
            q.append(i)

    if depth[a]<depth[b]:
        while depth[a]!=depth[b]:
            b=parents[b]
    else:
        while depth[a]!=depth[b]:
            a=parents[a]
    while a!=b:
        a=parents[a]
        b=parents[b]
    print(a)