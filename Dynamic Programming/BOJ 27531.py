n=int(input())
data=[[] for _ in range(n+1)]

for _ in range(n):
    a,b,c=map(int,input().split())
    data[a]=[b,c]

visited=[0 for _ in range(n+1)]
answer=0
dpyes=[0 for _ in range(n+1)]
dpno=[0 for _ in range(n+1)]
for i in range(1,n+1):
    if not visited[i]:
        minval=1e10
        visited[i]=1
        if i==data[i][0]:
            answer+=data[i][1]
            continue
        elif i==data[data[i][0]][0]:
            answer+=min(data[i][1],data[data[i][0]][1])
            visited[data[i][0]]=1
            continue
        q=[i]
        temp=data[i][0]
        while temp!=i:
            q.append(temp)
            visited[temp]=1
            temp=data[temp][0]
        dpyes[q[0]]=data[q[0]][1]
        dpyes[q[1]]=dpyes[q[0]]+data[q[1]][1]
        dpno[q[0]]=1e10
        dpno[q[1]]=data[q[1]][1]
        value=1e10
        for j in range(2,len(q)):
            dpyes[q[j]]=min(dpyes[q[j-1]],dpyes[q[j-2]])+data[q[j]][1]
            dpno[q[j]]=min(dpno[q[j-1]],dpno[q[j-2]])+data[q[j]][1]
        answer+=min(dpyes[q[len(q)-1]],dpyes[q[len(q)-2]],dpno[q[len(q)-1]])

visited=[0 for _ in range(n+1)]


print(answer)