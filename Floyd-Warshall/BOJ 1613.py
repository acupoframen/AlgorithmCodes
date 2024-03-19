import sys
input=sys.stdin.readline
n,k=map(int,input().split())
data=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(k):
    a,b=map(int,input().split())
    data[a][b]=-1
    data[b][a]=1
s=int(input())
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or k==i or k==j:
                continue
            if data[i][j]==-1 and data[j][k]==-1:
                data[i][k]=-1
                data[k][i]=1
            elif data[i][k]==-1==data[k][j]:
                data[i][j]=-1
                data[j][i]=1
            elif data[j][i]==-1 and data[i][k]==-1:
                data[j][k]=-1
                data[k][j]=1
            elif data[j][k]==-1==data[k][i]:
                data[j][i]=-1
                data[i][j]=1
            elif data[k][i]==-1==data[i][j]:
                data[k][j]=-1
                data[j][k]=1
            elif data[k][j]==-1==data[j][i]:
                data[k][i]=-1
                data[i][k]=1
                    
for i in range(s):
    a,b=map(int,input().split())
    if data[a][b]==-1:
        print(-1)
    elif data[a][b]==0:
        print(0)
    else:
        print(1)