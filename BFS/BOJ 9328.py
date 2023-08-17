from collections import deque
t=int(input())
import sys
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def search():
    global answer    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and data[nx][ny]!="*" and not visited[nx][ny]:
                if data[nx][ny].isupper():
                    num=ord(data[nx][ny])-ord('A')
                    if keyfound[num]:
                        visited[nx][ny]=1
                        q.append([nx,ny])
                    else:
                        door[num].append([nx,ny])
                else:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    if data[nx][ny]=="$":
                        answer+=1
                    elif data[nx][ny].islower():
                        num=ord(data[nx][ny])-ord('a')
                        keyfound[num]=1
                        for x1,y1 in door[num]:
                            q.append([x1,y1])
                            visited[x1][y1]=True    
for _ in range(t):
    answer=0
    h,w=map(int,input().strip().split())
    visited=[[0]*w for _ in range(h)]
    data=[list(input().strip()) for _ in range(h)]
    keyfound=[0 for _ in range(26)]
    door=[[] for _ in range(26)]
    key=input().strip()
    q=deque()
    if key=="0":
        pass
    else:
        for i in key:
            num=ord(i)-ord('a')
            keyfound[num]=1
    for i in range(h):
        for j in range(w):
            if i==0 or i==h-1 or j==0 or j==w-1:
                if data[i][j]!='*':
                    if data[i][j].isupper():
                        num=ord(data[i][j])-ord('A')
                        door[num].append([i,j])
                    else:
                        visited[i][j]=1
                        if data[i][j]=="$":
                            answer+=1
                        elif data[i][j].islower():
                            num=ord(data[i][j])-ord('a')
                            keyfound[num]=1
                        q.append([i,j])
    for i in range(26):
        if keyfound[i]:
            for j in door[i]:
                q.append(j)
    search()
    print(answer)