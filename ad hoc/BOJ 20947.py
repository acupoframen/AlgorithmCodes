n=int(input())
data=list(list(input()) for _ in range(n))
o=[]
x=[]
for i in range(n):
    for j in range(n):
        if data[i][j]=='O':
            o.append([i,j])
        elif data[i][j]=='X':
            x.append([i,j])


for a,b in x:
    for i in range(a-1,-1,-1):
        if data[i][b]=='.' or data[i][b]=='B':
            data[i][b]='B'
        else:
            break
    for i in range(a+1,n):
        if data[i][b]=='.' or data[i][b]=='B':
            data[i][b]='B'
        else:
            break
    for j in range(b-1,-1,-1):
        if data[a][j]=='.' or data[a][j]=='B':
            data[a][j]='B'
        else:
            break
    for j in range(b+1,n):
        if data[a][j]=='.' or data[a][j]=='B':
            data[a][j]='B'
        else:
            break

for a,b in o:    
    for i in range(a-1,-1,-1):
        if data[i][b]=='B':
            data[i][b]='.'
        elif data[i][b]=='.':
            pass
        else:
            break
    for i in range(a+1,n):
        if data[i][b]=='B':
            data[i][b]='.'
        elif data[i][b]=='.':
            pass
        else:
            break
    for j in range(b-1,-1,-1):
        if data[a][j]=='B':
            data[a][j]='.'
        elif data[a][j]=='.':
            pass
        else:
            break
    for j in range(b+1,n):
        if data[a][j]=='B':
            data[a][j]='.'
        elif data[a][j]=='.':
            pass
        else:
            break

for i in range(n):
    print(*data[i],sep="")