r,c,n=map(int,input().split())
data=[list(input()) for _ in range(r)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bomb(answergrid):
    bombbeddata=[['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if answergrid[i][j]=='O':
                bombbeddata[i][j]='.'
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<r and 0<=ny<c:
                        bombbeddata[nx][ny]='.'
    return bombbeddata
if not n%2:
    for _ in range(r):
        print("O"*c)
elif n==1:
    for i in range(r):
        print(''.join(data[i]))
elif n%4==3:
    answergrid=bomb(data)
    for i in range(r):
        print(''.join(answergrid[i]))
elif n%4==1:
    answergrid=bomb(data)
    answergrid=bomb(answergrid)
    for i in range(r):
        print(''.join(answergrid[i]))