n=int(input())
data=list(map(int,input().split()))
counts=[0 for _ in range(int(1e6)+1)]
stack=[]
answer=[-1 for _ in range(n)]
for i in data:
    counts[i]+=1

for i in range(n):
    while stack and counts[data[stack[-1]]]<counts[data[i]]:
        answer[stack.pop()]=data[i]
    stack.append(i)

print(*answer)