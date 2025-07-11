n,m=map(int,input().split())
dx=[[0,1],[1,1],[1,1],[0,1]]
dy=[[1,1],[0,-1],[0,1],[-1,-1]]
data=list(list(map(int,input().split())) for _ in range(n))
visited=[[0]*m for _ in range(n)]
answer=0
def dfs(x,y,count):
    global answer
    answer=max(answer,count)
    if x==n:
        return
    if not visited[x][y]:
        for k in range(4):
            x1,y1=x+dx[k][0],y+dy[k][0]
            x2,y2=x+dx[k][1],y+dy[k][1]
            if 0<=x1<n and 0<=y1<m and 0<=x2<n and 0<=y2<m:
                if not visited[x1][y1] and not visited[x2][y2]:
                    visited[x][y]=visited[x1][y1]=visited[x2][y2]=1
                    if y==m-1:
                        dfs(x+1,0,count+data[x][y]+data[x1][y1]*2+data[x2][y2])
                    else:
                        dfs(x,y+1,count+data[x][y]+data[x1][y1]*2+data[x2][y2])
                    visited[x][y]=visited[x1][y1]=visited[x2][y2]=0
    if y==m-1:
        dfs(x+1,0,count)
    else:
        dfs(x,y+1,count)
dfs(0,0,0)
print(answer)