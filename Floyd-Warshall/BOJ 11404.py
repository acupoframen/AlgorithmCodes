import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
data=[[1e10 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    i,j,val=map(int,input().split())
    data[i][j]=min(data[i][j],val)

for i in range(1,n+1):
    data[i][i]=1e10
answer=data[:]
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                continue
            answer[i][j]=min(answer[i][j],data[i][k]+data[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if answer[i][j]==1e10:
            print(0, end=" ")
        else:
            print(answer[i][j], end=' ')
    print()
