n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
startend=list(list(map(int,input().split())) for _ in range(m))
sumdata=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sumdata[i][j]=sumdata[i-1][j]+sumdata[i][j-1]-sumdata[i-1][j-1]+data[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2=startend[i]
    print(sumdata[x2][y2]-sumdata[x1-1][y2]-sumdata[x2][y1-1]+ sumdata[x1-1][y1-1])