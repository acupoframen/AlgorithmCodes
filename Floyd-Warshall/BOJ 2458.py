import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(0 for _ in range(n+1)) for _ in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not data[i][j]:
                if data[i][k] and data[k][j]:
                    data[i][j]=1
answer=0
for i in range(1,n+1):
    temp=0
    for j in range(1,n+1):
        temp+=data[i][j]+data[j][i]
    if temp==n-1:
        answer+=1
print(answer)