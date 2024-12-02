from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
time=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while True:
    icecount=0
    visited=list(list(0 for _ in range(m)) for _ in range(n))
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and data[i][j]>0:
                q = deque()
                q.append([i,j])
                visited[i][j] = 1
                icecount+=1
                while q:
                    x, y = q.popleft() 
                    for k in range(4):
                        nx, ny = x + dx[k], y+ dy[k]
                        if (0 <= nx < n and 0 <= ny < m):
                            if data[nx][ny] == 0:  
                                visited[x][y] += 1  
                            if visited[nx][ny] == 0 and data[nx][ny] != 0:  # 현 위치 주변이 빙산
                                q.append([nx, ny])
                                visited[nx][ny] = 1
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                data[i][j] -= (visited[i][j] - 1)
                if data[i][j] < 0:
                    data[i][j] = 0

    if icecount >= 2:
        print(time)
        break

    if icecount == 0:
        print(0)
        break

    time += 1  