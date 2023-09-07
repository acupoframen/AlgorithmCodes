r,c=map(int,input().split())
data=[]
for _ in range(r):
    data.append(list(input()))

possiblecoord=[]
for i in range(r):
    for j in range(c):
        if data[i][j]=='.':
            possiblecoord.append([i,j])

dx=[[0,-1],[0,1],[1,0],[-1,0]]
for a,b in possiblecoord:
    count=0
    for i in range(4):
        nx=a+dx[i][0]
        ny=b+dx[i][1]
        if 0<=nx<r and 0<=ny<c:
            if data[nx][ny]=='.':
                count+=1
    if count==1:
        print(1)
        exit(0)

print(0)