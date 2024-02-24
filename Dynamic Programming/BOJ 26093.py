import heapq
n,k=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
pastanswer=[[0,-1],[0,-1]]
for i in range(n):
    first,firstindex=pastanswer[0]
    second,secondindex=pastanswer[1]
    q=[]
    for j in range(k):
        if j!=firstindex:
            heapq.heappush(q,[-first-data[i][j],j])
        else:
            heapq.heappush(q,[-second-data[i][j],j])
    first,firstindex=heapq.heappop(q)
    second,secondinex=heapq.heappop(q)
    pastanswer=[[-first,firstindex],[-second,secondindex]]
print(-first)