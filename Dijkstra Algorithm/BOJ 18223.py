import heapq
v,e,p=map(int,input().split())
data=list([] for _ in range(v+1))
for _ in range(e):
    a,b,c=map(int,input().split())
    data[a].append((b,c))
    data[b].append((a,c))
dist=[1e10 for _ in range(v+1)]
q=[]
heapq.heappush(q,[0,1,0]) #cost,node,gunwoo
if p==1:
    print("SAVE HIM")
    exit(0)
mindist=1e10
while q:
    cost,curr,gunwoo=heapq.heappop(q)
    if cost>mindist:
        break
    if curr==v:
        mindist=cost
        if gunwoo==1:
            print("SAVE HIM")
            exit(0)
        continue
    if dist[curr]<cost:
        continue
    for i in data[curr]:
        if dist[i[0]]>=cost+i[1]:
            dist[i[0]]=cost+i[1]
            if i[0]==p:
                heapq.heappush(q,[dist[i[0]],i[0],1])
            else:
                heapq.heappush(q,[dist[i[0]],i[0],gunwoo])

print("GOOD BYE")