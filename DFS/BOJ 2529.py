n=int(input())
data=list(input().split())
visited=[False]*10
answer=[]
def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j
def dfs(count,temp):
    if count==n+1:
        answer.append(temp)
        return
    for i in range(10):
        if not visited[i]:
            if not count or check(temp[-1],str(i),data[count-1]):
                visited[i]=1
                dfs(count+1,temp+str(i))
                visited[i]=0
dfs(0,"")
print(answer[-1])
print(answer[0])
print(answer)