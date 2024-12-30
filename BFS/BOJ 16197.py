from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(input().strip()) for _ in range(n))
coin=deque()
coin.append([0])
for i in range(n):
    for j in range(m):
        if data[i][j]=="o":
            coin[0].append([i,j])

dx=[-1,0,0,1]
dy=[0,-1,1,0]

while coin:
    move,c1,c2=coin.popleft()
    for k in range(4):
        fall=0
        nx1=c1[0]+dx[k]
        ny1=c1[1]+dy[k]
        nx2=c2[0]+dx[k]
        ny2=c2[1]+dy[k]
        if not (0<=nx1<n and 0<=ny1<m):
            fall+=1
        if not (0<=nx2<n and 0<=ny2<m):
            fall+=1
        if fall==1:
            print(move+1)
            exit(0)
        if not fall:
            if data[nx1][ny1]=='#':
                nx1=c1[0]
                ny1=c1[1]
            if data[nx2][ny2]=='#':
                nx2=c2[0]
                ny2=c2[1]
            if not (nx1==nx2 and ny1==ny2):
                if move<=8:
                    coin.append([move+1,[nx1,ny1],[nx2,ny2]])
print(-1)