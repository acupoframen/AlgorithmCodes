n,m=map(int,input().split())
data=list(list(0 for _ in range(n+1)) for _ in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[a][b]=1
    data[b][a]=1
answer=0
for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n+1):
            if not data[i][j] and not data[j][k] and not data[i][k]:
                answer+=1
print(answer)