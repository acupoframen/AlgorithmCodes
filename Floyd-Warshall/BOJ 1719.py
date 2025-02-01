import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(1e10 for _ in  range(n+1)) for _ in range(n+1))
answer=list(list(0 for _ in range(n+1)) for _ in range(n+10))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            data[i][j]=0
            answer[i][j]=1e10
for _ in range(m):
    x,y,k=map(int,input().split())
    data[x][y]=k
    data[y][x]=k
    answer[x][y]=y
    answer[y][x]=x
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if data[a][b]>data[a][k]+data[k][b]:
                data[a][b]=data[a][k]+data[k][b]
                answer[a][b]=answer[a][k]
for i in range(1,n+1):
    for j in range(1,n+1):
        if answer[i][j]==1e10:
            print("-",end=" ")
        else:
            print(answer[i][j], end=" ")
    print()