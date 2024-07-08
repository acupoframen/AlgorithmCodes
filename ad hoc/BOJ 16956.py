r,c=map(int,input().split())
data=list(list(input()) for _ in range(r))
dx=[-1,0,0,1]
dy=[0,-1,1,0]
for i in range(r):
    for j in range(c):
        if data[i][j]=='S':
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<r and 0<=ny<c and data[nx][ny]=='W':
                    print("0")
                    exit(0)
for i in range(r):
    for j in range(c):
        if data[i][j]=='.':
            data[i][j]='D'
print(1)
for i in range(r):
    print("".join(data[i]))