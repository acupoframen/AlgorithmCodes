n,m=map(int,input().split())
data=list(list(map(int,list(input()))) for _ in range(n))
answer=0
for i in range(n):
    for j in range(m):
        if i>0 and j>0 and data[i][j]:
            data[i][j]+=min(data[i][j-1],data[i-1][j],data[i-1][j-1])
        answer=max(answer,data[i][j])
print(answer**2)