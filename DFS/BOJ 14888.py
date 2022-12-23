n=int(input())
data=list(map(int,input().split()))
cal=list(map(int,input().split()))
answer=[]
visited=[0]*(n-1)
calList=[]
for i in range(4):
    for j in range(cal[i]):
        calList.append(i)
calListOrdered=[]
def dfs(num):
    if num==n-1:
        number=data[0]
        for i in range(n-1):
            if calListOrdered[i]==0:
                number+=data[i+1]
            elif calListOrdered[i]==1:
                number-=data[i+1]
            elif calListOrdered[i]==2:
                number*=data[i+1]
            else:
                number/=data[i+1]
                number=int(number)
        answer.append(number)
        
    for i in range(n-1):
        if not visited[i]:
            visited[i]=1
            calListOrdered.append(calList[i])
            dfs(num+1)
            visited[i]=0
            calListOrdered.pop()

dfs(0)

print(max(answer))
print(min(answer))
