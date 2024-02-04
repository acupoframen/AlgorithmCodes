import heapq
c,n=map(int,input().split())
chicken=list(int(input()) for _ in range(c))
chicken.sort()
q=[]
for _ in range(n):
    a,b=map(int,input().split())
    heapq.heappush(q,[b,a])
answer=0
visited=[0 for _ in range(c)]
while q:
    b,a=heapq.heappop(q)
    for i in range(c):
        if a<=chicken[i]<=b and not visited[i]:
            visited[i]=1
            answer+=1
            break
print(answer)