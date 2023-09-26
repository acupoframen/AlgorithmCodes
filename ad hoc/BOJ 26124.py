h,w=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(h))
answer=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(h):
    for j in range(w):
        if data[i][j]==-1 or data[i][j]==0:
            continue
        biglampflag=1
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<h and 0<=ny<w:
                if data[nx][ny]==-1:
                    continue
                if not -1<=data[nx][ny]-data[i][j]<=1:
                    biglampflag=0
                    print(-1)
                    exit(0)
                if data[i][j]<data[nx][ny]:
                    biglampflag=0
                    break
        if biglampflag==1:
            answer+=1

print(answer)
