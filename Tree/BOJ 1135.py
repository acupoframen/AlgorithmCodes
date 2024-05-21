n=int(input())

data=list(map(int,input().split()))
tree=list([] for _ in range(n+1))
for i,boss in enumerate(data):
    if boss!=-1:
        tree[boss].append(i)

answer=[0 for _ in range(n)]

def dfs(i):
    temp=[]
    for slave in tree[i]:
        dfs(slave)
        temp.append(answer[slave])
    if temp:
        temp.sort(reverse=True)
        time=[temp[i]+i+1 for i in range(len(temp))]
        answer[i]=max(time)

dfs(0)
print(answer[0])