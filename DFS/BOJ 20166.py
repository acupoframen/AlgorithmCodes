import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
data=list(list(input()) for _ in range(n))
dx=[-1,0,0,1,-1,-1,1,1]
dy=[0,-1,1,0,1,-1,1,-1]

def move(x,y,d,str):
    if data[x][y]==s[d]:
        for i in range(8):
            nx=(x+dx[i])%n
            ny=(y+dy[i])%m
            answer[d][x][y]+=answer[d-1][nx][ny]
for _ in range(k):
    s=input().strip()
    answer=list(list(list(0 for _ in range(m)) for _ in range(n)) for _ in range(len(s)))
    for i in range(n):
        for j in range(m):
            if data[i][j]==s[0]:
                answer[0][i][j]=1
    for k in range(1,len(s)):
        for i in range(n):
            for j in range(m):
                move(i,j,k,str)
    count=0
    for i in range(n):
        for j in range(m):
            count+=answer[len(s)-1][i][j]
    print(count)