n,m=map(int,input().split())
data=list(list(list(list(input()))) for _ in range(n))
found=list(list(list(0 for _ in range(m)) for _ in range(n)) for _ in range(4))
answer=0

for i in range(1,n-1):
    for j in range(1,m-1):
        if data[i][j]=='.':
            if data[i][j+1]=='.':
                if data[i+1][j]=='X' and data[i+1][j+1]=='X' and not found[0][i][j]:
                    found[0][i][j]=1
                    found[0][i][j+1]=1
                    answer+=1
                if data[i-1][j] == 'X' and data[i-1][j+1] == 'X' and not found[1][i][j]:
                    found[1][i][j] = 1
                    found[1][i][j+1] = 1
                    answer += 1
            if data[i+1][j] == '.':
                if data[i][j+1] == 'X' and data[i+1][j+1] == 'X' and not found[2][i][j]:
                    found[2][i][j] = 1
                    found[2][i+1][j] = 1
                    answer += 1
                if data[i][j-1] == 'X' and data[i+1][j-1] == 'X' and not found[3][i][j]:
                    found[3][i][j] = 1
                    found[3][i+1][j] = 1
                    answer += 1
print(answer)