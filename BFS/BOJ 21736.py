from collections import deque
n,m=map(int,input().split())
data=list((list(input())) for _ in range(n))

def find():
    for i in range(n):
        for j in range(m):
            if data[i][j]=='I':
                return i,j

x,y=find()
dx=[-1,1,0,0]
dy=[0,0,1,-1]
visited=list([0 for _ in range(m)] for _ in range(n))
q=deque()
q.append([x,y])
visited[x][y]=1
answer=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<m and data[nx][ny]!='X' and not visited[nx][ny]:
            q.append([nx,ny])
            visited[nx][ny]=1
            if data[nx][ny]=='P':
                answer+=1

if answer:
    print(answer)
else:
    print("TT")