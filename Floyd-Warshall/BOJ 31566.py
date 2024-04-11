import sys
input=sys.stdin.readline
n,m,q=map(int,input().split())
data=list(list(list(1e10 for _ in range(n+1)) for _ in range(n+1)) for _ in range(n+1))
for _ in range(m):
    b,t,c=map(int,input().split())
    for j in range(1,n+1):
        if j==b or j==t:
            continue
        data[j][b][t]=c

for skip in range(1,n+1):
    for k in range(1,n+1):
        if k==skip:
            continue
        for i in range(1,n+1):
            if i==skip:
                continue
            for j in range(1,n+1):
                data[skip][i][j]=min(data[skip][i][j],data[skip][i][k]+data[skip][k][j])

for _ in range(q):
    s,k,e=map(int,input().split())
    if data[k][s][e]==1e10:
        print("No")
    else:
        print(data[k][s][e])