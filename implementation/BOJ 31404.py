h,w=map(int,input().split())
x,y,d=map(int,input().split())
a=list(list(map(int,list(input()))) for _ in range(h))
b=list(list(map(int,list(input()))) for _ in range(h))
dust=list(list(1 for _ in range(w)) for _ in range(h))
visited=list(list(list(0 for _ in range(4)) for _ in range(w)) for _ in range(h))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
answer=0
temp=0
beforecycle=0
while True:
    if dust[x][y]:
        dust[x][y]=0
        d=(d+a[x][y])%4
        temp+=1
        beforecycle=0
    else:
        d=(d+b[x][y])%4
        if visited[x][y][d]==temp:
            break
        visited[x][y][d]=temp
        beforecycle+=1
    x+=dx[d]
    y+=dy[d]
    answer+=1
    if not 0<=x<h or not 0<=y<w:
        break
print(answer-beforecycle)