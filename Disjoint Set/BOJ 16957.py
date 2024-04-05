r,c=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(r))
minloc=[[[i,j] for j in range(c)] for i in range(r)]

def find(x,y):
    if minloc[x][y]!=[x,y]:
        minloc[x][y]=find(*minloc[x][y])
    return minloc[x][y]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[0,1,-1,1,-1,1,0,-1]
for i in range(r):
    for j in range(c):
        x,y=i,j
        for k in range(8):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<r and 0<=ny<c:
                if data[x][y]>data[nx][ny]:
                    x,y=nx,ny
        minloc[i][j]=minloc[x][y]
x
answer=[[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        a,b=find(i,j)
        answer[a][b]+=1
for i in range(r):
    for j in range(c):
        print(answer[i][j],end=" ")
    print()