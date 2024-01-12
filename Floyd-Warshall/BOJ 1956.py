import sys
input=sys.stdin.readline
v,e=map(int,input().split())
data=list(list(1e10 for i in range(v+1)) for _ in range(v+1))
for _ in range(e):
    a,b,c=map(int,input().split())
    data[a][b]=c

answer=1e11
for k in range(1,v+1):
    for i in range(1,1+v):
        for j in range(1,1+v):
            if data[i][j]>data[i][k]+data[k][j]:
                data[i][j]=data[i][k]+data[k][j]

for i in range(1,v+1):
    for j in range(1,v+1):
        answer=min(answer,data[i][j]+data[j][i])

if answer>=1e10:
    print(-1)
else:
    print(answer)