n,m=map(int,input().split())
data=list(input() for _ in range(n))
dx=[-1,-1,1,1,0,0]
dy1=[0,1,0,1,-1,1]
dy2=[-1,0,-1,0,-1,1]
answer=0
for i in range(n):
    for j in range(m):
        if data[i][j]=='#':
            continue
        for k in range(6):
            if i%2==0:
                dy=dy2
            else:
                dy=dy1
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<n and 0<=ny<m and data[nx][ny]=='#':
                answer+=1
print(answer)
