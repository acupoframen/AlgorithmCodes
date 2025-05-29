import sys
input = sys.stdin.readline

r, c, K = map(int, input().split())
data = []
data = [list(input().rstrip()) for _ in range(r)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, k):
    global answer
    if x == 0 and y == (c-1) and k == K:
        answer += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and data[nx][ny]!='T':
            data[nx][ny] = 'T' 
            dfs(nx, ny, k+1)
            data[nx][ny] = '.' 

data[r-1][0] = 'T'
dfs(r-1, 0, 1) 
print(answer)