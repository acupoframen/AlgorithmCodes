n,m,x,y,k=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
commands=list(map(int,input().split()))
dx=[[0,0],[1,0],[-1,0],[0,-1],[0,1]]
frontback=[0,0]
leftright=[0,0]
topbottom=[0,0]
x,y=y,x
for i in range(k):
    if 0<=x+dx[commands[i]][0]<m and 0<=y+dx[commands[i]][1]<n:
        x,y=x+dx[commands[i]][0],y+dx[commands[i]][1]
        if commands[i]==1:
            temp=leftright
            leftright=topbottom[::-1]
            topbottom=temp
        elif commands[i]==2:
            temp=leftright
            leftright=topbottom
            topbottom=temp[::-1]
        elif commands[i]==3:
            temp=frontback
            frontback=topbottom[::-1]
            topbottom=temp
        else:
            temp=frontback
            frontback=topbottom
            topbottom=temp[::-1]
        if data[y][x]==0:
            data[y][x]=topbottom[1]
        else:
            topbottom[1]=data[y][x]
            data[y][x]=0
        print(topbottom[0])