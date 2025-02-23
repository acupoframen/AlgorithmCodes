n=int(input())
limits=list(map(int,input().split()))
data=list(list(map(int,input().split())) for _ in range(n))
answer=1e10
answerlist=[]
def dfs(status,curr,depth,price):
    global answer,answerlist
    flag=1
    for i in range(4):
        if status[i]<limits[i]:
            flag=0
            break
    if flag:
        if answer>price:
            answer=price
            answerlist=curr[:]
        elif price == answer and curr < answerlist:
            answerlist = curr[:]
        return
    if depth>=n:
        return
    dfs(status,curr,depth+1,price)
    for i in range(4):
        status[i]+=data[depth][i]
    curr.append(depth)
    dfs(status,curr,depth+1,price+data[depth][4])
    curr.pop()
    for i in range(4):
        status[i]-=data[depth][i]
dfs([0,0,0,0],list(),0,0)
if answer==1e10:
    print(-1)
    exit(0)
print(answer)
print(*list(map(lambda x:x+1,answerlist)))