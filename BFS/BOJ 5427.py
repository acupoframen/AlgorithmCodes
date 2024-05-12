from collections import deque
dx=[-1,0,0,1]
dy=[0,1,-1,0]
t=int(input())
for _ in range(t):
    w,h=map(int,input().split())
    data=list(list(input()) for _ in range(h))
    visited=list(list(0 for _ in range(w)) for _ in range(h))
    sang=deque()
    fire=deque()
    flag=0
    for i in range(h):
        for j in range(w):
            if data[i][j]=="@":
                sang.append([i,j,0])
                visited[i][j]=1
                data[i][j]="."
            elif data[i][j]=='*':
                fire.append([i,j,0])
    while sang:
        x,y,val=sang.popleft()
        
        if fire and fire[0][2]==val-1:
            while True:
                firex,firey,firec=fire.popleft()
                if firec==val:
                    fire.appendleft([firex,firey,firec])
                    break
                for k in range(4):
                    nx=firex+dx[k]
                    ny=firey+dy[k]
                    if 0<=nx<h and 0<=ny<w and data[nx][ny]==".":
                        data[nx][ny]='*'
                        fire.append([nx,ny,firec+1])
        if data[x][y]=='*':
            continue
        if x in [0,h-1] or y in [0,w-1]:
            print(val+1)
            flag=1
            break
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<h and 0<=ny<w and data[nx][ny]=='.' and not visited[nx][ny]:
                sang.append([nx,ny,val+1])
                visited[nx][ny]=1
    if not flag:
        print("IMPOSSIBLE")