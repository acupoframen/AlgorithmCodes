import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
data=list(list(input().strip()) for _ in range(n))
b=list(list(0 for _ in range(m+1)) for _ in range(n+1))
w=list(list(0 for _ in range(m+1)) for _ in range(n+1))
for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            if data[i][j]=="B":
                b[i+1][j+1]=b[i][j+1]+b[i+1][j]-b[i][j]+1
                w[i+1][j+1]=w[i][j+1]+w[i+1][j]-w[i][j]
            else:
                w[i+1][j+1]=w[i][j+1]+w[i+1][j]-w[i][j]+1
                b[i+1][j+1]=b[i][j+1]+b[i+1][j]-b[i][j]
        else:
            if data[i][j]=="B":
                w[i+1][j+1]=w[i][j+1]+w[i+1][j]-w[i][j]+1
                b[i+1][j+1]=b[i][j+1]+b[i+1][j]-b[i][j]
            else:
                b[i+1][j+1]=b[i][j+1]+b[i+1][j]-b[i][j]+1
                w[i+1][j+1]=w[i][j+1]+w[i+1][j]-w[i][j]
answer=1e10
for i in range(n-k+1):
    for j in range(m-k+1):
        bcnt=b[i+k][j+k]-b[i][j+k]-b[i+k][j]+b[i][j]
        wcnt=w[i+k][j+k]-w[i][j+k]-w[i+k][j]+w[i][j]
        answer=min(answer,bcnt,wcnt)
print(answer)