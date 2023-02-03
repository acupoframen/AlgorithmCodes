from collections import deque
import sys
input=sys.stdin.readline
n,l,r=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
dx=[[1,0],[-1,0],[0,1],[0,-1]]
def bfs(y,x):
    connected=[]
    connected.append([y,x])
    q=deque()
    q.append([y,x])
    while q:
        y,x=q.popleft()
        visited[y][x]=1
        for i in range(4):
            ny=y+dx[i][0]
            nx=x+dx[i][1]
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                if l<=abs(data[ny][nx]-data[y][x])<=r:
                    visited[ny][nx]=1
                    connected.append([ny,nx])
                    q.append([ny,nx])
    return connected
def answerFinder(li):
    value=0
    for a,b in li:
        value+=data[a][b]
    people=len(li)
    if people ==1:
        return 0
    while li:
        y,x=li.pop()
        data[y][x]=(value//people)
    return 1
answer=0
while True:
    q=deque()
    popMove=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if answerFinder(bfs(i,j)):
                    popMove=1
    if popMove:
        answer+=1
    else:
        break
print(answer)
