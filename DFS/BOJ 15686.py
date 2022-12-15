import sys
input=sys.stdin.readline
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

n,m=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            house.append([i,j])
        elif data[i][j]==2:
            chicken.append([i,j])
dists=[]
for i in range(len(house)):
    tempL=list()
    for j in range(len(chicken)):
        tempL.append(dist(house[i],chicken[j]))
    dists.append(tempL)

score=1e10
visited=[False]*len(dists[0])
def dfs(temp,latest):
    global score
    if len(temp)==m:
        
        setscore=0
        for n1 in range(len(dists)):
            comp=1e10
            for n2 in range(len(dists[0])):
                if n2 in temp:
                    comp=min(comp,dists[n1][n2])
            setscore+=comp
        score=min(setscore,score)
        return
    for i in range(latest,len(dists[0])):

        if not visited[i]:
            visited[i]=True
            temp.append(i)
            latest+=1
            dfs(temp,latest)
            visited[i]=False
            temp.pop()
        
dfs([],0)
print(score)

