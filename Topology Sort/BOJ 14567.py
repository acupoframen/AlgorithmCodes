import heapq
n,m=map(int,input().split())
degree= [ 0 for _ in range(n+1)]
data=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    degree[b]+=1

answer=[0 for _ in range(n+1)]
q=[]
for i in range(1,n+1):
    if degree[i]==0:
        heapq.heappush(q,i)
        answer[i]=1

while q:
    a=heapq.heappop(q)
    if data[a]:
        for i in data[a]:
            answer[i]=max(answer[a]+1,answer[i])
            degree[i]-=1
            if degree[i]==0:
                
                heapq.heappush(q,i)
print(*answer[1:])