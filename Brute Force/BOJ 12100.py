from copy import deepcopy
def up(data):
    for i in range(n):
        currval=0
        currloc=0
        for j in range(n):
            if data[j][i] ==0:
                continue
            if currval==0:
                currval=data[j][i]
                data[j][i]=0
            elif currval==data[j][i]:
                data[currloc][i]=currval*2
                currval=0
                currloc+=1
                data[j][i]=0
            else:
                data[currloc][i]=currval
                currval=data[j][i]
                currloc+=1
                data[j][i]=0
        if currval!=0:
            data[currloc][i]=currval
    return data
def down(data):
    for i in range(n):
        currloc=n-1
        currval=0
        for j in range(n-1,-1,-1):
            if data[j][i]==0:
                continue
            if currval==0:
                currval=data[j][i]
                data[j][i]=0
            elif currval==data[j][i]:
                data[currloc][i]=currval*2
                currval=0
                currloc-=1
                data[j][i]=0
                
            else:
                data[currloc][i]=currval
                currval=data[j][i]
                currloc-=1
                data[j][i]=0
        if currval!=0:
            data[currloc][i]=currval
    return data


def left(data):
    for i in range(n):
        currloc=0
        currval=0
        for j in range(n):
            if data[i][j]==0:
                continue
            if currval==0:
                currval=data[i][j]
                data[i][j]=0
            elif currval==data[i][j]:
                data[i][currloc]=currval*2
                currval=0
                currloc+=1
                data[i][j]=0
                
            else:
                data[i][currloc]=currval
                currval=data[i][j]
                currloc+=1
                data[i][j]=0
        if currval!=0:
            data[i][currloc]=currval
    return data

def right(data):
    for i in range(n):
        currloc=n-1
        currval=0
        for j in range(n-1,-1,-1):
            if data[i][j]==0:
                continue
            if currval==0:
                currval=data[i][j]
                data[i][j]=0
            elif currval==data[i][j]:
                data[i][currloc]=currval*2
                currval=0
                currloc-=1
                data[i][j]=0
            else:
                data[i][currloc]=currval
                currval=data[i][j]
                currloc-=1
                data[i][j]=0
        if currval!=0:
            data[i][currloc]=currval
    return data


def left(data):
    for i in range(n):
        currloc=0
        currval=0
        for j in range(n):
            if data[i][j]==0:
                continue
            if currval==0:
                currval=data[i][j]
                data[i][j]=0
            elif currval==data[i][j]:
                data[i][currloc]=currval*2
                currval=0
                currloc+=1
                data[i][j]=0
                
            else:
                data[i][currloc]=currval
                currval=data[i][j]
                currloc+=1
                data[i][j]=0
        if currval!=0:
            data[i][currloc]=currval
    return data

answer=0
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
def dfs(data1,count):
    global answer
    if count==5:
        for i in range(n):
            for j in range(n):
                answer=max(answer,data1[i][j])
        return
    dfs(up(deepcopy(data1)),count+1)
    dfs(down(deepcopy(data1)),count+1)
    dfs(left(deepcopy(data1)),count+1)
    dfs(right(deepcopy(data1)),count+1)

dfs(data,0)
print(answer)