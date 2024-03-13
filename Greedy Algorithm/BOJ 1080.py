n,m=map(int,input().split())

ori=list(list(map(int,input())) for _ in range(n))
new=list(list(map(int,input())) for _ in range(n))

if n<=2 or m<=2:
    for i in range(n):
        for j in range(m):
            if ori[i][j]!=new[i][j]:
                print(-1)
                exit(0)
    
    print(0)
    exit(0)

answer=0
for i in range(n-2):
    for j in range(m-2):
        if ori[i][j]!=new[i][j]:
            answer+=1
            for i1 in range(3):
                for j1 in range(3):
                    if ori[i+i1][j+j1]==1:
                        ori[i+i1][j+j1]=0
                    else:
                        ori[i+i1][j+j1]=1
for i in range(n):
    for j in range(m):
        if ori[i][j]!=new[i][j]:
            print(-1)
            exit(0)

print(answer)