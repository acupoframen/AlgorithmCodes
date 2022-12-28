from collections import deque
m,n= map(int,input().split())
data=[[1e10]*n]
for i in range(m):
    data.append([1e10]+list(map(int,list(input()))))
visited=[[[0,0] for _ in range(n+1)] for _ in range(m+1)]


q=deque()
q.append([1,1,0])
visited[1][1]=[1,1]
dx=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs():
    if n==1 and m==1:
        return 1
    while q:
        x,y,brokenWall=q.popleft()
        for x1,y1 in dx:
            if 0<x+x1<m+1 and 0<y+y1<n+1:
                if x+x1==m and y+y1==n: 
                    return visited[x][y][brokenWall]+1
                if not visited[x+x1][y+y1][brokenWall]:
                    if not data[x+x1][y+y1]: 
                        visited[x+x1][y+y1][brokenWall]=visited[x][y][brokenWall]+1
                        q.append([x+x1,y+y1,brokenWall])
                    if not brokenWall and data[x+x1][y+y1]:  
                        visited[x+x1][y+y1][1]=(visited[x][y][brokenWall]+1)
                        q.append([x+x1,y+y1,1])
                        
                            
    return -1

print(bfs())
