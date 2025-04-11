dx=[1,0,-1,0]
dy=[0,1,0,-1]
n=int(input())
target=int(input())
data=list(list(0 for _ in range(n)) for _ in range(n))
now=n**2
x=0
y=0
d=0
nx=0
ny=0
target_x=0
target_y=0
while now>0:
    data[x][y]=now
    if now==target:
        target_x=x+1
        target_y=y+1
    now-=1
    nx=x+dx[d] 
    ny=y+dy[d]
    if nx<0 or nx>=n or ny<0 or ny>=n or data[nx][ny]!=0:
        d=(d+1)%4
    x=x+dx[d] 
    y=y+dy[d]
for i in range(n):
    print(*data[i])
print(target_x,target_y)