from collections import deque
n,m=map(int,input().split())
indegree=[0]*(n+1)
arr=[[] for _ in range(n+1)]

for i in range(m):
    temp=list(map(int,input().split()))
    for j in range(1,temp[0]):
        arr[temp[j]].append(temp[j+1])
        indegree[temp[j+1]]+=1

result=[]
queue=deque()

for i in range(1,n+1):
    if not indegree[i]:
        queue.append(i)

while queue:
    temp=queue.popleft()
    result.append(temp)
    for i in arr[temp]:
        indegree[i]-=1
        if not indegree[i]:
            queue.append(i)

if len(result)==n:
    for i in result:
        print(i)

else:
    print(0)