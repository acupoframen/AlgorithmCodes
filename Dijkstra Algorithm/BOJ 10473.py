import heapq
startx,starty=map(float,input().split())
endx,endy=map(float,input().split())
n=int(input())
data=[]
data.append([startx,starty])
for _ in range(n):
    a,b=map(float,input().split())
    data.append([a,b])
data.append([endx,endy])
dist=[[1e10 for _ in range(n+2)] for _ in range(n+2) ]
time=[[1e10 for _ in range(n+2)] for _ in range(n+2) ]
q=[[0,0]]
for i in range(1,n+2):
    dist[0][i]=((data[i][0]-data[0][0])**2+(data[i][1]-data[0][1])**2)**0.5
    time[0][i]=dist[0][i]/5

for i in range(1,n+2):
    for j in range(1,n+2):
        if i==j:
            continue
        dist[i][j]=((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2)**0.5
        if dist[i][j]<=50:
            time[i][j]=min(dist[i][j]/5,(50-dist[i][j])/5+2)
        else:
            time[i][j]=min(dist[i][j]/5,(dist[i][j]-50)/5+2)

timetables=[1e10 for _ in range(n+2)]
timetables[0]=0
while q:
    t,place=heapq.heappop(q)
    if timetables[place]<t:
        continue
    if place==n+1:
        print(t)
        break
    for i in range(n+2):
        if place==i:
            continue
        if t+time[place][i]<timetables[i]:
            heapq.heappush(q,[t+time[place][i],i])
            timetables[i]=t+time[place][i]
