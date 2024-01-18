import sys
sys.setrecursionlimit(10**6)
n=int(input())
data=list(list(0 for _ in range(1000)) for _ in range(1000))

dx=[-1,-1,1,1,1,-1]
dy=[0,1,1,0,-1,-1]
possibleroute=[[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]]
answer=0
def dfs(x,y,i,d):
    global answer
    if i==n:
        if data[x][y]==1:
            answer+=1
        return
    if data[x][y]:
        return
    data[x][y]=1
    dfs(x+dx[possibleroute[d][0]],y+dy[possibleroute[d][0]],i+1,possibleroute[d][0])
    dfs(x+dx[possibleroute[d][1]],y+dy[possibleroute[d][1]],i+1,possibleroute[d][1])
    data[x][y]=0

data[501][500]=1
dfs(500,500,0,0)

print(answer)