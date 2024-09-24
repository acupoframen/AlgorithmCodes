n,m=map(int,input().split())
data=list(list(input()) for _ in range(n))
answer=0

for i in range(n):
    flag=0
    for j in range(m):
        if data[i][j]=='-':
            if flag==0:
                answer+=1
                flag=1
            if flag==1:
                continue
        else:
            flag=0

for i in range(m):
    flag=0
    for j in range(n):
        if data[j][i]=='|':
            if flag==0:
                answer+=1
                flag=1
            if flag==1:
                continue
        else:
            flag=0
print(answer)           