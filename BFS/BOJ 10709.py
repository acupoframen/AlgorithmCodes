from collections import deque
h,w=map(int,input().split())
answer=[[-1 for _ in range(w)] for _ in range(h)]
cloudcoords=deque()
for i in range(h):
    line=input()
    for j in range(len(line)):
        if line[j]=='c':
            cloudcoords.append([i,j,0])
while cloudcoords:
    a,b,t=cloudcoords.popleft()
    if answer[a][b]==-1:
        answer[a][b]=t
        if b+1<w:
            cloudcoords.append([a,b+1,t+1])
for i in range(h):
    for j in range(w):
        print(answer[i][j],end=' ')
    print()