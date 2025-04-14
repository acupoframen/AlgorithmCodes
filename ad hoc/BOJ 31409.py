n=int(input())
data=[0]+list(map(int,input().split()))
visited=data[:]
answer=0
for i in range(1,n+1):
    if i==1 and data[i]==1:
        visited[i]=2
        answer+=1
    elif data[i]==i:
        visited[i]=1
        answer+=1
print(answer)
print(*visited[1:])