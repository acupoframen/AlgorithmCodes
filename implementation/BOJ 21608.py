import sys
input=sys.stdin.readline
import heapq
dx=[-1,0,0,1]
dy=[0,1,-1,0]
n=int(input())
table=[[0]*n for _ in range(n)]
likeInfo=dict()
for _ in range(n**2):
    info=list(map(int,input().split()))
    likeInfo[info[0]]=set(info[1:])
def satis():
    result=0
    for i in range(n):
        for j in range(n):
            if not table[i][j]:
                continue
            count=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if table[nx][ny] in likeInfo[table[i][j]]:
                        count+=1
            if count:
                result+= 10**(count-1)
    return result
def insert(idx):
    q=[]
    for i in range(n):
        for j in range(n):
            if not table[i][j]:
                likeCount, emptyCount=0,0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if table[nx][ny] in likeInfo[idx]:
                            likeCount+=1
                        if not table[nx][ny]:
                            emptyCount+=1
                heapq.heappush(q,(-likeCount,-emptyCount,i,j))
    likeCount,emptyCount,i,j=heapq.heappop(q)
    table[i][j]=idx

for i in likeInfo.keys():
    insert(i)
print(satis())