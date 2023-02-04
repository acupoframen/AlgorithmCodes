from collections import deque
import sys
import copy
input=sys.stdin.readline
dx=[[-1,0],[1,0],[0,1],[0,-1]]
n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if data[i][j]==2:
            q.append([i,j])

def wall(number):
    if number==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if not data[i][j]:
                data[i][j]=1
                wall(number+1)
                data[i][j]=0

def bfs():
    global answer
    queue=copy.deepcopy(q)
    bfsmap=copy.deepcopy(data)
    while queue:
        x,y=queue.popleft()
        for a,b in dx:
            if 0<=a+x<n and 0<=b+y<m: 
                nx=a+x
                ny=b+y
                if not bfsmap[nx][ny]:
                    bfsmap[nx][ny]=2
                    queue.append([nx,ny])
    count=0
    for i in range(n):
        for j in range(m):
            if not bfsmap[i][j]:
                count+=1
    answer=max(answer,count)
    return
answer=0
wall(0)
print(answer)