from copy import deepcopy
r,c,t=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(r))
aircon=0
for i in range(r):
    if data[i][0]==-1:
        aircon=i
        break
dx=[[-1,0],[1,0],[0,-1],[0,1]]
for _ in range(t):
    temp=[[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if data[i][j]==-1:
                continue
            if data[i][j]:
                sides=0
                for a,b in dx:
                    if 0<=a+i<r and 0<=b+j<c:
                        if data[a+i][b+j]!=-1:
                            temp[a+i][b+j]+=data[i][j]//5
                            sides+=1
                temp[i][j]+=(data[i][j]-((data[i][j]//5)*sides))
    for i in range(aircon-1,0,-1):
        temp[i][0]=temp[i-1][0]
    for i in range(c-1):
        temp[0][i]=temp[0][i+1]
    for i in range(0,aircon):
        temp[i][c-1]=temp[i+1][c-1]
    for i in range(c-1,0,-1):
        temp[aircon][i]=temp[aircon][i-1]

    for i in range(aircon+2,r-1):
        temp[i][0]=temp[i+1][0]
    for i in range(1,c):
        temp[r-1][i-1]=temp[r-1][i]
    for i in range(r-2,aircon,-1):
        temp[i+1][c-1]=temp[i][c-1]
    for i in range(c-2,0,-1):
        temp[aircon+1][i+1]=temp[aircon+1][i]
    temp[aircon+1][1]=0
    temp[aircon][0]=-1
    temp[aircon+1][0]=-1
    temp[aircon][1]=0
    data=deepcopy(temp)
answer=0
for i in range(r):
    answer+=sum(data[i])

print(answer+2)