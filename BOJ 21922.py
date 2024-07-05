from collections import deque
import sys
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0] 
# e, w , s , n
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))

def move(k):
    if k==1:
        return [5,5,2,3]
    if k==2:
        return [0,1,5,5]
    if k==3:
        return [3,2,1,0]
    if k==4:
        return [2,3,0,1]
    if k==0:
        return [0,1,2,3]
    if k==9:
        return [5,5,5,5]
visited=list(list(list(0  for _ in range(4))for _ in range(m)) for _ in range(n))
answer=list(list(0 for _ in range(m)) for _ in range(n))

for i in range(n):
    for j in range(m):
        if data[i][j]==9:
            q=deque()
            answer[i][j]=1
            for k in range(4):
                q.append([i,j,k])
            while q:
                x,y,dir=q.popleft()
                
                answer[x][y]=1
                if dir==5:
                    continue
                if visited[x][y][dir]:
                    continue
                visited[x][y][dir]=1
                nx=x+dx[dir]
                ny=y+dy[dir]
                if 0<=nx<n and 0<=ny<m:
                    answer[i][j]=1
                    newdir=move(data[nx][ny])[dir]
                    q.append([nx,ny,newdir])

realanswer=0
for i in range(n):
    realanswer+=sum(answer[i])
print(realanswer)