from collections import deque
n=int(input())
log=n.bit_length()
data=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])

tree=[[[0,0] for _ in range(log)] for _ in range(n+1)]
level=[-1 for _ in range(n+1)]
q=deque()
q.append(1)
level[1]=0
while q:
    a=q.popleft()
    for nextnode, dist in data[a]:
        if level[nextnode]!= -1:
            continue
        level[nextnode]= level[a]+1
        tree[nextnode][0][0]=a
        tree[nextnode][0][1]=dist
        q.append(nextnode)

for i in range(1,log):
    for j in range(1,n+1):
        a=tree[tree[j][i-1][0]] [i-1][0]
        dist=tree[j][i-1][1] + tree[tree[j][i-1][0]][i-1][1]
        tree[j][i]=[a,dist]

m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    d=0
    if level[a]<level[b]:
        a,b=b,a
    for i in range(log-1,-1,-1):
        if level[a]-level[b]>= 2**i:
            d+=tree[a][i][1]
            a=tree[a][i][0]

    if a==b:
        print(d)
        continue

    for i in range(log-1,-1,-1):
        if tree[a][i][0] != tree[b][i][0]:
            d+=(tree[a][i][1]+tree[b][i][1])
            a=tree[a][i][0]
            b=tree[b][i][0]
    d+=(tree[a][0][1]+tree[b][0][1])
    print(d)