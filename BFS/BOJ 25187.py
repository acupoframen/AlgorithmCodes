import sys
input=sys.stdin.readline
from collections import deque
n,m,q=map(int,input().split())
values=[0]+list(map(int,input().split()))
data=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
visited=[False for _ in range(n+1)]
waterData=[1e10 for _ in range(n+1)] 
def BFS(num):
    q=deque([num])
    group=[]
    answer=0
    while q:
        i=q.popleft()
        if not visited[i]:
            group.append(i)
            visited[i]=True
            if not values[i]:
                answer-=1
            else:
                answer+=1
            for j in data[i]:
                q.append(j)
    for i in group:
        waterData[i]=answer

for _ in range(q):
    num=int(input())
    if waterData[num]==1e10:
        BFS(num)
    if waterData[num]>0:
        print(1)
    else:
        print(0)