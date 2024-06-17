import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
maxval=201
minval=-1
data=[]
for _ in range(n):
    temp=[]
    for j in list(map(int,input().split())):
        maxval=max(maxval,j)
        minval=min(minval,j)
        temp.append(j)
    data.append(temp)
start=data[0][0]
end=data[n-1][n-1]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def check(mid):
    for i in range(minval,maxval+1):
        if not (i<=start<=i+mid and i<=end<=i+mid):
            continue
        if bfs(i,i+mid):
            return True
    return False

def bfs(a,b):
    visited=list(list(0 for _ in range(n)) for _ in range(n))
    visited[0][0]=1
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        if x==n-1 and y==n-1:
            return True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                number=data[nx][ny]
                if not a<=number<=b:
                    continue
                visited[nx][ny]=1
                q.append([nx,ny])

left=0
right=maxval
answer=0
while left<=right:
    mid=(left+right)//2
    if check(mid):
        answer=mid
        right=mid-1
    else:
        left=mid+1
print(answer)