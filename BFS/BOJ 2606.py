from collections import deque
compN=int(input())
dataN=int(input())
computers=list([] for _ in range(compN+1))
visited=[False]*(compN+1)
for _ in range(dataN):
    key, value= map(int, input().split())
    computers[key].append(value)
    computers[value].append(key)
q=deque()
q.append(1)

answer=0
while q:
    num=q.popleft()
    if not visited[num]:
        answer+=1
        visited[num]=True
        for j in computers[num]:
            q.append(j)
            
        
print(answer-1)
