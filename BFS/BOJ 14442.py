from collections import deque
n,m,k=map(int,input().split())
data=list(list(map(int,list(input()))) for _ in range(n))
dp=list(list(list(1e10 for _ in range(m)) for _ in range(n)) for _ in range(k+1))
q=deque()
q.append([0,0,0,0]) #x,y,wallbreaks, count
dx=[-1,0,0,1]
dy=[0,-1,1,0]
dp[0][0][0]=0
while q:
    x,y,w,count=q.popleft()
    if x==n-1 and y==m-1:
        print(dp[w][x][y]+1)
        exit(0)
    if count>dp[w][x][y]:
        continue
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny]==1:
                if w<k:
                    if count+1<dp[w+1][nx][ny]:
                        dp[w+1][nx][ny]=count+1
                        q.append([nx,ny,w+1,count+1])
            else:
                if count+1<dp[w][nx][ny]:
                    dp[w][nx][ny]=count+1
                    q.append([nx,ny,w,count+1])

print(-1)   