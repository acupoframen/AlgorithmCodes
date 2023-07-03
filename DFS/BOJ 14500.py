import sys
input=sys.stdin.readline
n,m=map(int,input().split())
sum=0
data=[]
dx=[[-1,0],[1,0],[0,-1],[0,1]]
for i in range(n):
    data.append(list(map(int,input().split())))

visited=[[False for _ in range (m)] for _ in range(n)]
def dfs(x,y,k,value):
    global sum
    if k==4:
        sum=max(sum,value)
        return
    for i,j in dx:
        nx=i+x
        ny=y+j
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                visited[nx][ny]=True
                if k==2:
                    dfs(x,y,k+1,value+data[nx][ny])
                dfs(nx,ny,k+1,value+data[nx][ny])
                visited[nx][ny]=False
for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,1,data[i][j])
        visited[i][j]=False


print(sum)