n,m=map(int,input().split())
q,*qdata=map(int,input().split())
k,*kdata=map(int,input().split())
p,*pdata=map(int,input().split())
data=[[1 for _ in range(m)] for _ in range(n)]
location=[[0 for _ in range(m)] for _ in range(n)]
for i in range(q):
    a,b=qdata[i*2]-1,qdata[i*2+1]-1
    location[a][b]=1
    data[a][b]=0

for i in range(k):
    a,b=kdata[i*2]-1,kdata[i*2+1]-1
    location[a][b]=1
    data[a][b]=0

for i in range(p):
    a,b=pdata[i*2]-1,pdata[i*2+1]-1
    location[a][b]=1
    data[a][b]=0
for i in range(q):
    a,b=qdata[i*2]-1,qdata[i*2+1]-1
    for i in range(a-1,-1,-1):
        if location[i][b]==0:
            data[i][b]=0
        else:
            break
    for i in range(a+1,n,1):
        if location[i][b]==0:
            data[i][b]=0
        else:
            break

    for i in range(b-1,-1,-1):
        if location[a][i]==0:
            data[a][i]=0
        else:
            break
        
    for i in range(b+1,m,1):
        if location[a][i]==0:
            data[a][i]=0
        else:
            break
    i=a+1;j=b+1
    while 0<=i<n and 0<=j<m:
        if location[i][j]==1:
            break
        data[i][j]=0
        i+=1
        j+=1
    i=a-1;j=b-1
    while 0<=i<n and 0<=j<m:
        if location[i][j]==1:
            break
        data[i][j]=0
        i-=1
        j-=1
    i=a-1;j=b+1
    while 0<=i<n and 0<=j<m: 
        if location[i][j]==1:
            break
        data[i][j]=0
        i-=1
        j+=1

    i=a+1;j=b-1
    while 0<=i<n and 0<=j<m:
        if location[i][j]==1:
            break
        data[i][j]=0
        i+=1
        j-=1

for i in range(k):
    a,b=kdata[i*2]-1,kdata[i*2+1]-1
    dx=[[-2,-1],[-2,1],[2,-1],[2,1],[1,2],[1,-2],[-1,2],[-1,-2]]
    for j in range(8):
        if 0<=a+dx[j][0]<n and 0<=b+dx[j][1]<m:
            data[a+dx[j][0]][b+dx[j][1]]=0

for i in range(p):
    a,b=pdata[i*2]-1,pdata[i*2+1]-1
    data[a][b]=0

answer=0
for i in range(n):
    answer+=sum(data[i])
print(data)
print(answer)