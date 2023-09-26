n,m=map(int,input().split())
data=list(list(input()) for _ in range(n))
for i in range(n):
    for j in range(m//2):
        if data[i][j]!='.' or data[i][m-j-1]!='.':
            if data[i][j]=='.':
                data[i][j]=data[i][m-j-1]
            else:
                data[i][m-j-1]=data[i][j]
for i in range(n):
    print(''.join(data[i]))