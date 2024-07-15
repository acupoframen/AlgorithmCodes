from collections import deque
answer=0
data=list(list(input()) for _ in range(12))
dx=[-1,0,0,1]
dy=[0,1,-1,0]
while True:
    flag=0
    visited=list(list(0 for _ in range(6)) for _ in range(12))
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and data[i][j]!='.':
                currblock=data[i][j]
                visited[i][j]=1
                q=deque()
                q.append([i,j])
                count=1
                temp=[]
                while q:
                    x,y=q.popleft()
                    temp.append([x,y])
                    for k in range(4):
                        nx=dx[k]+x
                        ny=dy[k]+y 
                        if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny]:
                            if data[nx][ny]==currblock:
                                count+=1
                                q.append([nx,ny])
                                visited[nx][ny]=1
                if count>=4:
                    flag=1
                    for x,y in temp:
                        data[x][y]='.'

    if flag==1:
        answer+=1
        for y in range(6):
            for x in range(11,-1,-1):
                tempx=x
                if data[x][y]!='.':
                    while tempx+1<=11 and data[tempx+1][y]=='.':
                        data[tempx+1][y]=data[tempx][y]
                        data[tempx][y]='.'
                        tempx+=1

    else:
        break
print(answer)