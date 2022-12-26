from collections import deque
m,n,box=map(int,input().split())
data=list([0]*n for _ in range(m))
for _ in range(box):
    a,b,c,d=map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            data[j][i]=1
dx=[[-1,0],[1,0],[0,1],[0,-1]]
sizes=[]
q=deque()
for i in range(m): 
    for j in range(n):
        if not data[i][j]:
            size=0
            data[i][j]=1
            q.append([i,j])
            while q:
                x1,y1=q.popleft()
                size+=1
                for k in dx:
                    
                    if 0<=x1+k[0]<m and 0<=y1+k[1]<n and not data[x1+k[0]][y1+k[1]]:
                        data[x1+k[0]][y1+k[1]]=1
                        q.append([x1+k[0],y1+k[1]])
                        
            sizes.append(size)
        

print(len(sizes))
print(*sorted(sizes))
