import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
connect=[[] for _ in range(n+1)]
need=[[0 for _ in range(n+1)] for _ in range(n+1)]
q=deque()
degree=[0 for _ in range(n+1)]

m=int(input())
for _ in range(m):
    x,y,k=map(int,input().split())
    connect[y].append([x,k])
    degree[x]+=1

for i in range(1,n+1):
    if not degree[i]:
        q.append(i)

while q:
    num=q.popleft()
    for next,nexting in connect[num]:
        if sum(need[num])==0:
            need[next][num]+=nexting
        else:
            for i in range(1,n+1):
                need[next][i]+=need[num][i]*nexting
        degree[next]-=1
        if not degree[next]:
            q.append(next)

for i in range(1,n):
    if need[n][i]:
        print(i,need[n][i])