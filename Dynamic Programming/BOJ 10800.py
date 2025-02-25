from collections import defaultdict
n=int(input())
data=list()
for i in range(n):
    a,b=map(int,input().split())
    data.append([a,b,i])
data.sort(key=lambda x: x[1])
answer=defaultdict(int)
ballsize=defaultdict(int)
total=0
idx=0
for i in range(n):
    while data[idx][1]<data[i][1]:
        total+=data[idx][1]
        ballsize[data[idx][0]]+=data[idx][1]
        idx+=1
    answer[data[i][2]]=total-ballsize[data[i][0]]
for i in range(n):
    print(answer[i])