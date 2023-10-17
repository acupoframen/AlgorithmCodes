from collections import deque
n,k=map(int,input().split())
q=deque([i for i in range(1,n+1)])
answer=[]
while q:
    for _ in range(k-1):
        num=q.popleft()
        q.append(num)
    answer.append(q.popleft())

print("<",end="")
for i in answer[:len(answer)-1]:
    print(i,",", sep="",end=" ")
print(answer[-1],">",sep="")