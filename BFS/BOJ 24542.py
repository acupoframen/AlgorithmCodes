from collections import deque
n,m=map(int,input().split())
data=list([] for _ in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
visited=[0 for _ in range(n+1)]
answer=1
for i in range(1,n+1):
    num=1
    if not visited[i]:
        q=deque([i])
        num=1
        while q:
            n=q.popleft()
            visited[n]=1
            for a in data[n]:
                if not visited[a]:
                    q.append(a)
                    visited[a]=1
                    num+=1
    
    answer*=num  
print(answer%1000000007) 
