n,k=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
x,y=map(int,input().split())
answer=1e10
if abs(x)+abs(y)<=k:
    answer=min(abs(x)+abs(y),answer)
for i in range(n):
    if abs(data[i][0]-x)+abs(data[i][1]-y)+2<=k:
        answer=min(abs(data[i][0]-x)+abs(data[i][1]-y)+2,answer)
data.sort()
tries=[]
if k==4:
    tries.append([x,y,0])
if k==5:
    tries.append([x,y,0])
    tries.append([x-1,y,1])
    tries.append([x+1,y,1])
    tries.append([x,y+1,1])
    tries.append([x,y-1,1])

for i in range(n):
    a,b=data[i]
    for j in range(len(tries)):
        goalx,goaly=tries[j][0]-a,tries[j][1]-b
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if data[mid][0]<goalx:
                left=mid+1
            elif data[mid][0]>goalx:
                right=mid-1
            else:
                if data[mid][1]>goaly:
                    right=mid-1
                elif data[mid][1]<goaly:
                    left=mid+1
                else:
                    answer=min(answer,4+tries[j][2])
                    break
if answer>k:
    print(-1)
else:
    print(answer)