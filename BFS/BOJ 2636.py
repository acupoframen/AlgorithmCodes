from collections import deque
n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,0],[1,0],[0,1],[0,-1]
day=0
q=deque()
day=0
pastCheese=0
def bfs():
    while True:
        q.append([0,0])
        cheese=0
        flag=0
        global day
        global pastCheese
        while q:
            newCoord=q.popleft()
            for a,b in dx:
                if 0<=newCoord[0]+a<n and 0<=newCoord[1]+b<m:
                    if data[newCoord[0]+a][newCoord[1]+b]==0:
                        data[newCoord[0]+a][newCoord[1]+b]=1e10
                        q.append([newCoord[0]+a,newCoord[1]+b])
                    elif data[newCoord[0]+a][newCoord[1]+b]==1:
                        data[newCoord[0]+a][newCoord[1]+b]=-1
                        cheese+=1
        if not cheese:
            cheese=pastCheese
            return pastcheese
        day+=1
        pastcheese=cheese
        for i in range(n):
            for j in range(m):
                if data[i][j]==-1:
                    data[i][j]=0
                    flag=1
                    
                elif data[i][j]==1e10:
                    data[i][j]=0
cheese=bfs()
print(day)
print(cheese)
