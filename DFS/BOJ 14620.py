n=int(input())
dir=[[0,0],[1,0],[0,1],[-1,0],[0,-1]]
data=list(list(map(int,input().split())) for _ in range(n))
answer=1e10
visited=list(list(0 for _ in range(n)) for _ in range(n))
def check(x,y):
    global n
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
            return False
    return True

def calc(x,y):
    result=0
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        result+=data[nx][ny]
    return result

def dfs(cost,depth):
    global answer
    if depth==3:
        answer=min(answer,cost)
        return
    for i in range(n):
        for j in range(n):
            if check(i,j):
                visited[i][j]=True
                for dx,dy in dir:
                    visited[i+dx][j+dy]=True
                dfs(cost+calc(i,j),depth+1)
                for dx,dy in dir:
                    visited[i+dx][j+dy]=False
dfs(0,0)
print(answer)