n,m=map(int,input().split())
data=[list(input()) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]

answer=0
c=0
def dfs(x,y,c):
    global answer
    if visited[x][y]:
        if visited[x][y]==c:
            answer+=1
        return
    visited[x][y]=c
    nx=x
    ny=y
    if data[x][y]=='D':
        nx+=1
    elif data[x][y]=='U':
        nx-=1
    elif data[x][y]=='L':
        ny-=1
    else:
        ny+=1
    dfs(nx,ny,c)
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            c+=1
            dfs(i,j,c)

print(answer)