from collections import deque
n,k=map(int,input().split())
visited=[0 for _ in range(200001)]
q=deque()
q.append([n,0])
answercount=0
answertime=1e10
while q:
    location,time=q.popleft()
    visited[location]=1
    if location==k:
        if answertime>time:
            answertime=time
            answercount=1
        elif answertime==time:
            answercount+=1
    if 0<=location-1<=200000:
        if not visited[location-1]:
            q.append([location-1,time+1])
    if 0<=location+1<=200000:
        if not visited[location+1]:
            q.append([location+1,time+1])
    if 0<=2*location<=200000:
        if not visited[location*2]:
            q.append([location*2,time+1])
print(answertime)
print(answercount)