from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
h,w,startx,starty,endx,endy=map(int,input().split())
startx-=1
starty-=1
endx-=1
endy-=1
q=deque()
visited=list(list(0 for _ in range(m-w+1)) for _ in range(n-h+1))

for i in range(startx,startx+h):
    for j in range(starty,starty+w):
        if data[i][j]:
            print(-1)
            exit(0)
visited[startx][starty]=1
q.append([startx,starty,[]])

dx=[-1,1,0,0]
dy=[0,0,-1,1] #u,d, l,r

while q:
    x,y,directions=q.popleft()
    if x==endx and y==endy:
        print(len(directions))
        exit(0)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not (0<=nx<=n-h and 0<=ny<=m-w):
            continue
        if visited[nx][ny]:
            continue
        flag=0
        if i==0:
            for k in range(w):
                if data[x-1][y+k]:
                    flag=1
                    break
        elif i==1:
            for k in range(w):
                if data[x+h][y+k]:
                    flag=1
                    break
        
        elif i==2:
            for k in range(h):
                if data[x+k][y-1]:
                    flag=1
                    break
        else:
            for k in range(h):
                if data[x+k][y+w]:
                    flag=1
                    break
        
        if not flag:
            visited[nx][ny]=1
            q.append([nx,ny,directions+[i]])
print(-1)