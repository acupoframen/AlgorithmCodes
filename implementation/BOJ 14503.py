n,m=map(int,input().split())
dx=[[-1,0],[0, 1],[1,0],[0,-1]]
r,c,d=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
data[r][c]=2
answer=1
def changedirection(d):
    if d==0:
        return 3
    else:
        return d-1

def solve(x,y,dir):
    global answer
    while True:
        check=False
        orid=dir
        for i in range(4):
            dir=changedirection(dir)
            nx,ny=x+dx[dir][0],y+dx[dir][1]
            if data[nx][ny]==0:
                x,y=nx,ny
                data[nx][ny]=2
                check=True
                answer+=1
                break
        if not check:
            backnx, backny=x-dx[orid][0],y-dx[orid][1]
            if data[backnx][backny]==1:
                return answer
            else:
                x,y=backnx,backny

print(solve(r,c,d))