import sys
import heapq
import math
input=sys.stdin.readline
n,m=map(int,input().strip().split())
data=list(list(input().strip()) for _ in range(n))
answer=[[math.inf for _ in range(m)] for _ in range(n)]
q=[]
for i in range(n):
    for j in range(m):
        if data[i][j]== "C":
            data[i][j]='F'
            answer[i][j]=0
            heapq.heappush(q,[0,i,j])
        elif data[i][j] == 'X':  
            li = i  
            temp = []  
            while li < n and data[li][j] == 'X':  
                temp.append([li, j])  
                li += 1  
            if data[li][j] == 'D':  
                for ti, tj in temp:  
                    data[ti][tj] = 'D'  
            else:  
                for ti, tj in temp:  
                    data[ti][tj] = [li, j]
dx=[-1,1]
while q:
    val,x,y=heapq.heappop(q)
    if val>answer[x][y]:
        continue
    if data[x][y]=='E':
        print(answer[x][y])
        exit(0)
    elif data[x][y]=='F':
        for d in range(2):
            ny=y+dx[d]
            if ny<0 or ny>=m:
                continue
            if data[x][ny]=='D':
                continue
            if answer[x][ny]>val+1:
                answer[x][ny]=val+1
                heapq.heappush(q,[val+1,x,ny])
        if x+1<n and data[x+1][y]=='L' and answer[x+1][y]>val+5:
            answer[x+1][y]=val+5
            heapq.heappush(q,[val+5,x+1,y])
    elif data[x][y]=='L':
        for d in range(2):
            ny=y+dx[d]
            if ny<0 or ny>=m:
                continue
            if data[x][ny]=='D':
                continue
            if answer[x][ny]>val+1:
                answer[x][ny]=val+1
                heapq.heappush(q,[val+1,x,ny]) 
        if x+1<n and data[x+1][y]=='L' and answer[x+1][y]>val+5:
            answer[x+1][y]=val+5
            heapq.heappush(q,[val+5,x+1,y])
        if x-1>=0 and not data[x-1][y]=='D' and not data[x-1][y]=='X' and answer[x-1][y]>val+5:
            answer[x-1][y]=val+5
            heapq.heappush(q,[val+5,x-1,y])
    else:
        ni = data[x][y][0]  
        nj = data[x][y][1]  
        if answer[ni][nj] > val + 10:  
            answer[ni][nj] = val + 10  
            heapq.heappush(q, [val+10, ni, nj])  
print('dodo sad')