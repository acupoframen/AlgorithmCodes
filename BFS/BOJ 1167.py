import sys
input=sys.stdin.readline
from collections import deque
v=int(input())
data=[[] for _ in range(v+1)]
for _ in range(1,v+1):
    a,*b,c=list(map(int,input().split()))
    for i in range(len(b)):
        if not i%2:
            data[a].append([b[i],b[i+1]])

def bfs(s):
    maxV=[0,0]
    visited=[-1 for _ in range(v+1)]
    q=deque()
    q.append(s)
    visited[s]=0
    while q:
        p=q.popleft()
        for a,b in data[p]:
            if visited[a]==-1:
                visited[a]=b+visited[p]
                q.append(a)
                if maxV[1]<visited[a]:
                    maxV=[a,visited[a]]
    return maxV

a,b=bfs(1)
answerA,answerB=bfs(a)
print(answerB)