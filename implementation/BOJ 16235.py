dx=[0,0,-1,-1,-1,1,1,1]
dy=[-1,1,0,-1,1,-1,0,1]
n,m,k=map(int,input().split())
data=[[5 for _ in range(n+1)] for _ in range(n+1)]
tree=[[[] for _ in range(n+1)] for _ in range(n+1)]
yangbun=[0]+list([0]+list(map(int,input().split())) for _ in range(n))

for i in range(m):
    x,y,z=map(int,input().split())
    tree[x][y].append(z)

for _ in range(k):
    temp=[]
    dead=[]
    #spring
    for i in range(1,n+1):
        for j in range(n+1):
            temp1=[]
            if tree[i][j]:
                tree[i][j].sort()
                for k in tree[i][j]:
                    if k<=data[i][j]:
                        data[i][j]-=k
                        k+=1
                        temp1.append(k)
                        if not k%5:
                            temp.append([i,j])  
                    else:
                        dead.append([i,j,k//2])
                tree[i][j]=temp1
    #summer
    for i,j,k in dead:
        data[i][j]+=k
    #fall
    for i,j in temp:
        for k in range(8):
            nx,ny = dx[k]+i, dy[k]+j
            if 1<=nx<=n and 1<=ny<=n:
                tree[nx][ny].append(1)
    #winter
    for i in range(1,n+1):
        for j in range(n+1):
            data[i][j]+=yangbun[i][j]
    

answer=0
for i in range(1,n+1):
    for j in range(1,n+1):
        answer+=len(tree[i][j])

print(answer)