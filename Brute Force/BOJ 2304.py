import sys
input= sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
data.sort()
mid=list(map(lambda x: x[1], data)).index(max(list(map(lambda x: x[1], data))))
currCoord=0
currHeight=0
answer=0
for i in range(mid+1):
    if currCoord==0:
        currCoord=data[i][0]
        currHeight=data[i][1]
    else:
        if i==mid:
            gap=data[i][0]-currCoord
            answer+=gap*currHeight
        elif currHeight<data[i][1]:
            gap=data[i][0]-currCoord
            answer+=gap*currHeight
            currHeight=data[i][1]
            currCoord=data[i][0]
        
currCoord=n-1
currHeight=0
for i in range(n-1,mid-1,-1):
    if currCoord==n-1:
        currCoord=data[i][0]+1
        currHeight=data[i][1]
    else:
        if i==mid:
            gap=currCoord-data[i][0]-1
            answer+=gap*currHeight
        elif currHeight<data[i][1]:
            gap=currCoord-data[i][0]-1
            answer+=gap*currHeight
            currHeight=data[i][1]
            currCoord=data[i][0]+1
answer+=max(list(map(lambda x: x[1], data)))
print(answer)
