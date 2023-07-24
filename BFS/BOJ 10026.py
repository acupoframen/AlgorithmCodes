from collections import deque
n=int(input())
data=list(list(input()) for _ in range(n))
visited=[[0 for _ in range(n)] for _ in range(n)]
dx=[[-1,0],[1,0],[0,1],[0,-1]]
answer=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            letter=data[i][j]
            q=deque()
            q.append([i,j])
            answer+=1
            while q:
                i1,j1=q.popleft()
                for a,b in dx:
                    if not 0<=i1+a<n or not 0<=j1+b<n:
                        continue
                    if not visited[i1+a][j1+b] and data[i1+a][j1+b]==letter:
                        visited[i1+a][j1+b]=1
                        q.append([i1+a,j1+b])
print(answer,end=' ')
answer=0
visited=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            letter=data[i][j]
            q=deque()
            q.append([i,j])
            answer+=1
            while q:
                i1,j1=q.popleft()
                for a,b in dx:
                    if not 0<=i1+a<n or not 0<=j1+b<n:
                        continue
                    if letter=='B':
                        if not visited[i1+a][j1+b] and data[i1+a][j1+b]==letter:
                            visited[i1+a][j1+b]=1
                            q.append([i1+a,j1+b])
                    else:
                        if not visited[i1+a][j1+b] and data[i1+a][j1+b]!='B':
                            visited[i1+a][j1+b]=1
                            q.append([i1+a,j1+b])
print(answer)