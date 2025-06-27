from collections import deque
n,k=map(int,input().split())
data=['']+list(input() for _ in range(n))
a,b=map(int,input().split())
answer=[]
q=deque()
q.append([a,[a]])
visited=list(0 for _ in range(n+1))
visited[a]=1
while q:
    x,path=q.popleft()
    if x==b:
        print(*path)
        exit(0)
    for i in range(1,n+1):
        cnt=0
        if not visited[i]:
            for j in range(k):
                if data[x][j]!=data[i][j]:
                    cnt+=1
                if cnt>1:
                    break
            if cnt==1:
                visited[i]=1
                q.append([i,path+[i]])
print(-1)