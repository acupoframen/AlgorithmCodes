n,k=map(int,input().split())
data=list(list(1 for _ in range(n+1)) for _ in range(n+1))
for i in range(2,n+1):
    for j in range(1,i):
        data[i][j]=(data[i-1][j-1]+data[i-1][j])%10007
print(data[n][k])