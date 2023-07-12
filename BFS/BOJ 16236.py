from collections import deque
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
def findStart():
    for i in range(n):
        for j in range(n):
            if data[i][j]==9:
                data[i][j]=0
                return [i,j]

curr=findStart()
sharkSize=2
dx=[[0,1],[0,-1],[1,0],[-1,0]]
time=0
eatenFish=0
while True:
    visited=[[False for _ in range(n)] for _ in range(n)]
    possiblePoints=[]
    foundWhen=0
    q=deque([[curr[0],curr[1],0]])
    while q:
        a,b,c=q.popleft()
        if possiblePoints and c>foundWhen:
            break
        for i in range(4):
            nx=a+dx[i][0]
            ny=b+dx[i][1]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if data[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append([nx,ny,c+1])
                elif sharkSize>data[nx][ny]:
                    possiblePoints.append([nx,ny,c+1])
                    visited[nx][ny]=True
                    foundWhen=c
                elif sharkSize==data[nx][ny]:
                    visited[nx][ny]=True
                    q.append([nx,ny,c+1])
    if not possiblePoints:
        print(time)
        break
    possiblePoints.sort()
    curr=possiblePoints[0]
    time+=(foundWhen+1)
    data[possiblePoints[0][0]][possiblePoints[0][1]]=0
    eatenFish+=1
    if eatenFish==sharkSize:
        sharkSize+=1
        eatenFish=0