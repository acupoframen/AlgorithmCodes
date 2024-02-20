data=list(list(map(int,input().split())) for _ in range(10))
papers=[0]+[5]*5
def possible (x,y):
    temp=[]
    for n in range(1,6):
        for i in range(x,x+n):
            for j in range(y,y+n):
                if i<0 or i>=10 or j<0 or j>=10 or data[i][j]==0:
                    return temp
        temp.append(n)
    return temp

answer=1e10
def color(x,y,n,val):
    for i in range(x,x+n):
        for j in range(y,y+n):
            data[i][j]=val


def dfs(space):
    global answer
    if space==0:
        answer=min(answer,25-sum(papers))
        return
    for i in range(10):
        for j in range(10):
            if data[i][j]==1:
                temp=possible(i,j)
                for num in temp[::-1]:
                    if papers[num]>0:
                        papers[num]-=1
                        color(i,j,num,0)
                        dfs(space-num**2)
                        papers[num]+=1
                        color(i,j,num,1)
                return

temp1=0
for i in range(10):
    for j in range(10):
        if data[i][j]==1:
            temp1+=1

dfs(temp1)
if answer!=1e10:
    print(answer)
else:
    print(-1)