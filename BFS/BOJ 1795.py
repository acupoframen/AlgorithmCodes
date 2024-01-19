from collections import deque
n,m=map(int,input().split())
data=list(list(input()) for _ in range(n))
horse=[]
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,2,-2,-2,2,-1,1]
for i in range(n):
    for j in range(m):
        if data[i][j]!='.':
            horse.append([i,j,data[i][j]])
answer=list(list(0 for _ in range(m)) for _ in range(n))
malcount=list(list(0 for _ in range(m)) for _ in range(n))
for x,y,val in horse:
    q=deque()
    q.append([x,y,val,1])
    visited=list(list(0 for _ in range(m)) for _ in range(n))
    visited[x][y]=1
    malcount[x][y]+=1
    while q:
        x,y,val1,count=q.popleft()
        if int(val1)==0:
            val1=val
            count+=1
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                q.append([nx,ny,int(val1)-1,count])
                malcount[nx][ny]+=1
                visited[nx][ny]=1
                answer[nx][ny]+=count

number=1e10
for i in range(n):
    for j in range(m):
        if malcount[i][j]==len(horse):
            number=min(number,answer[i][j])

if len(horse)==1:
    print(0)
elif number==1e10:
    print(-1)
else:
    print(number)