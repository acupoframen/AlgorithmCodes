from collections import deque
n=int(input())
data=list(list(input()) for _ in range(n))
heights=list(list(map(int, input().split()) ) for _ in range(n))
dx=[0,1,-1,0,1,1,-1,-1]
dy=[1,0,0,-1,1,-1,1,-1]
startx=0
starty=0
house=0
heights1d=set()
for i in range(n):
    for j in range(n):
        if data[i][j]=='P':
            startx=i
            starty=j
        if data[i][j]=='K':
            house+=1
        heights1d.add(heights[i][j])
heights1d=sorted(list(heights1d))
left=0
right=0
answer=1e10
while left<len(heights1d):
    visited=list(list(0 for _ in range(n)) for _ in range(n))
    q=deque()
    if heights1d[left]<=heights[startx][starty]<=heights1d[right]:
        visited[startx][starty]=1
        q.append([startx,starty])
    count=0
    while q:
        x,y=q.popleft()
        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if not visited[nx][ny] and heights1d[left]<=heights[nx][ny]<=heights1d[right]:
                if data[nx][ny]=='K':
                    count+=1
                visited[nx][ny]=1
                q.append([nx,ny])
    if count==house:
        answer=min(answer,heights1d[right]-heights1d[left])
        left+=1
    elif right+1<len(heights1d):
        right+=1
    else:
        break
print(answer)