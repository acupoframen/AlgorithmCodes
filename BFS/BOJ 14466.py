from collections import deque
n,k,r=map(int,input().split())

roads=list(list([] for _ in range(n+1)) for _ in range(n+1))

for i in range(r):
    a,b,c,d=map(int,input().split())
    roads[a][b].append([c,d])
    roads[c][d].append([a,b])

dx=[[0,1],[0,-1],[1,0],[-1,0]]
answer=[[[1 for _ in range(n+1)] for _ in range(n+1)] for k in range(n)]
cows=[]
for i in range(k):
    q=deque()
    a,b=map(int,input().split())
    visited=[[0 for _ in range(n+1)] for _ in range(n+1)]
    visited[a][b]=1
    cows.append([a,b])
    q.append([a,b])
    while q:
        a,b=q.popleft()
        for x,y in dx:
            nx=x+a
            ny=y+b
            if 0<nx<n+1 and 0<ny<n+1 and [nx,ny] not in roads[a][b] and not visited[nx][ny]:
                q.append([nx,ny])
                answer[i][nx][ny]=0
                visited[nx][ny]=1
    
finalanswer=0
for i in range(k):
    for j in range(i+1,k):
        a,b=cows[i]
        c,d=cows[j]
        if answer[i][c][d]==1:
            finalanswer+=1

print(finalanswer)