h,w,x,y=map(int,input().split())

data=[]
for i in range(h+x):
    data.append(list(map(int,input().split())))

datanew=[[0 for _ in range (w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i<x or i>=h or j<y or j>=w:
            datanew[i][j]=data[i][j]
        else:
            datanew[i][j] = data[i][j]-datanew[i-x][j-y]

for i in datanew:
    print(*i)