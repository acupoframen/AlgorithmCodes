from collections import deque
n=int(input())
data=list(list(input().split()) for _ in range(n))
dx=[[0,1],[1,0]]
q=deque()
q.append([data[0][0],0,1,'0'])
q.append([data[0][0],1,0,'0']) #currval,x,y,currop
minVal=1e10
maxVal=-1e10
while q:
    val,x,y,op=q.popleft()
    if x==n-1 and y==n-1:
        if op=='+':
            val=int(val)+int(data[x][y])
        elif op=='-':
            val=int(val)-int(data[x][y])
        else:
            val=int(val)*int(data[x][y])
        minVal=min(minVal,int(val))
        maxVal=max(maxVal,int(val))
        continue
    if (x+y)%2:
        for k in dx:
            nx=x+k[0]
            ny=y+k[1]
            if nx<n and ny<n:
                q.append([int(val),nx,ny,data[x][y]])
    else:
        for k in dx:
            nx=x+k[0]
            ny=y+k[1]
            if nx<n and ny<n:
                if op=='+':
                    q.append([int(val)+int(data[x][y]),nx,ny,'op'])
                elif op=='-':
                    q.append([int(val)-int(data[x][y]),nx,ny,'op'])
                else:
                    q.append([int(val)*int(data[x][y]),nx,ny,'op'])
print(maxVal,minVal)