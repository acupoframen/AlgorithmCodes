from collections import deque

r,c,k=map(int,input().split())
data=list(list(input()) for _ in range(r))
q=deque()
temp=list(list(0 for _ in range(c)) for _ in range(r))
temp[r-1][0]=1
q.append([temp,1,r-1,0])
answer=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
while q:
    temp,step,x,y = q.popleft()
    print(temp,step,x,y)
    if x==0 and y==c-1:
        if step==k:
            answer+=1
        continue
    if step>k:
        continue
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<r and 0<=ny<c and data[nx][ny]!='T' and not temp[nx][ny]:
            new_temp=[row[:] for row in temp]
            new_temp[nx][ny]=1
            q.append([new_temp,step+1,nx,ny])

print(answer)  