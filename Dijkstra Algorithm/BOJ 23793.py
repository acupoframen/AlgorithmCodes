import heapq
n,m=map(int,input().split())
data=list(list() for _ in range(n+1))

for _ in range(m):
    x,y,z=map(int,input().split())
    data[x].append([y,z])
x,y,z=map(int,input().split())
q=[]
length=list(1e12 for _ in range(n+1))
length[x]=0
heapq.heappush(q,[0,x]) #length, curr,crosscheck
while q:
    currlength,curr=heapq.heappop(q)
    if length[curr]<currlength:
        continue
    for next,nextlength in data[curr]:
        if length[next]>currlength+nextlength:
            length[next]=currlength+nextlength
            heapq.heappush(q,[length[next],next])
temp=length[y]
q=[]
length=list(1e12 for _ in range(n+1))
length[y]=0
heapq.heappush(q,[0,y]) #length, curr,crosscheck
while q:
    currlength,curr=heapq.heappop(q)
    if length[curr]<currlength:
        continue
    for next,nextlength in data[curr]:
        if length[next]>currlength+nextlength:
            length[next]=currlength+nextlength
            heapq.heappush(q,[length[next],next])
if length[z]+temp>=1e12:
    print(-1,end=" ")
else:
    print(length[z]+temp,end=" ")




q=[]
length=list(1e12 for _ in range(n+1))
length[x]=0
heapq.heappush(q,[0,x]) #length, curr
while q:
    currlength,curr=heapq.heappop(q)
    if length[curr]<currlength:
        continue
    for next,nextlength in data[curr]:
        if next==y:
            continue
        if length[next]>currlength+nextlength:
            length[next]=currlength+nextlength
            heapq.heappush(q,[length[next],next])
if length[z]==1e12:
    print(-1,end=" ")
else:
    print(length[z],end=" ")