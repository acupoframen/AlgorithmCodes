import sys
input=sys.stdin.readline
r,c=map(int,input().split())
data=list(list(input().strip()) for _ in range(r))
visited=list(list(0 for _ in range(c)) for _ in range(r))
dx=[-1,0,1]
def dfs(x,y):
    if y==c-1:
        return True
    for i in dx:
        nx=x+i
        ny=y+1
        if 0<=nx<r and 0<=ny<c:
            if data[nx][ny]!='x' and not visited[nx][ny]:
                visited[nx][ny]=1
                if dfs(nx,ny):
                    return True
    return False
answer=0
for i in range(r):
    if dfs(i,0):
        answer+=1
print(answer)