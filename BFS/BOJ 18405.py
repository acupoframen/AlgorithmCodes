from collections import deque
n,k=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
q=[]
for i in range(n):
    for j in range(n):
        if data[i][j]!=0:
            q.append([i,j,data[i][j],1])
q=deque(sorted(q[1:],key=lambda x:x[2]))
dx=[0,0,-1,1]
dy=[1,-1,0,0]
s,xx,yy=map(int,input().split())
xx-=1
yy-=1
while q:
    x,y,val,sec=q.popleft()
    if sec>s:
        break
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n and data[nx][ny]==0:
            data[nx][ny]=val
            q.append([nx,ny,val,sec+1])
print(data[xx][yy])