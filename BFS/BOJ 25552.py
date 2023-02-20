from collections import deque
a,b=map(int,input().split())
originalData=list(list(input()) for _ in range(a))
move=int(input())
changedData=list(list(input()) for _ in range(a))
oriq=deque()
for i in range(a):
    for j in range(b):
        if originalData[i][j]=='O':
            if changedData[i][j]=='X':
                print("NO")
                exit(0)
            oriq.append([i,j])
            changedData[i][j]='X'
dx=[1,0,0,-1]
dy=[0,-1,1,0]
visited=[[0]*b for _ in range(a)]
while oriq:
    orix,oriy=oriq.popleft()
    for i in range(orix-move,orix+move+1):
        for j in range(oriy-move,oriy+move+1):
            if 0<=i<a and 0<=j<b and abs(orix-i)+abs(oriy-j)<=move and not visited[i][j]:
                visited[i][j]=1
                if changedData[i][j]=='O':
                    changedData[i][j]='X'
                    oriq.append([i,j])
for i in range(a):
    for j in range(b):
        if changedData[i][j]=='O':
            print("NO")
            exit(0)
print("YES")