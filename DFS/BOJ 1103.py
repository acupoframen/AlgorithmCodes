import sys
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(input()))
visited=list(list(False for _ in range(m)) for _ in range(n))
dp=[[0 for _ in range(m)] for _ in range(n)]
result=0
def dfs(x,y,count):
    global result
    result=max(result,count)
    for i in range(4):
        nx=x+int(data[x][y])*dx[i]
        ny=y+int(data[x][y])*dy[i]
        if 0<=nx<n and 0<=ny<m and data[nx][ny]!="H" and count+1> dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny]=count+1
                visited[nx][ny]=True
                dfs(nx,ny,count+1)
                visited[nx][ny]=False
dfs(0,0,0)
print(result+1)