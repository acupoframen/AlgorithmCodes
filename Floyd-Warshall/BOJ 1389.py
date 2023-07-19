n,m=map(int,input().split())
data=[[n for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    data[a][b]=1
    data[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                data[i][j]=0
            else:
                data[i][j]=min(data[i][j],data[i][k]+data[k][j])

answer=[]
print(data)
for i in range(1,n+1):
    answer.append(sum(data[i]))
print(answer)
print(answer.index(min(answer))+1)