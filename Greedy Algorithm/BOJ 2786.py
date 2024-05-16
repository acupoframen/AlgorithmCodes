import heapq,math
n=int(input())
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
data.sort(key=lambda x:x[1])
temp=[0 for _ in range(n)]
answer=[math.inf for _ in range(n)]
current=0

temp[-1]=data[-1][0]
for i in range(n-2,-1,-1):
    temp[i]=min(temp[i+1],data[i][0])

for i in range(n):
    answer[i]=min(answer[i],current+temp[i])
    current+=data[i][1]
q=[]
current=0
for i in range(n):
    current+=data[i][1]
    heapq.heappush(q,data[i][0]-data[i][1])
    answer[i]=min(answer[i],current+q[0])
for i in answer:
    print(i)