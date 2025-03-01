from itertools import combinations
comblist=list(combinations(range(6),2))

def f(data):
    global answer
    answer=0
    for i in range(18):
        if data[i]<0 or data[i]>5:
            return 0
    dfs([0 for _ in range(18)],0)
    return answer

def dfs(result,d):
    global answer,data
    if d==15:
        if result==data:
            answer=1
        return
    for i in range(18):
        if result[i]>data[i]:
            return
    i,j=comblist[d]
    result[i*3]+=1
    result[j*3+2]+=1
    dfs(result,d+1)
    result[i*3]-=1
    result[j*3+2]-=1

    result[i*3+1]+=1
    result[j*3+1]+=1
    dfs(result,d+1)
    result[i*3+1]-=1
    result[j*3+1]-=1

    result[i*3+2]+=1
    result[j*3]+=1
    dfs(result,d+1)
    result[i*3+2]-=1
    result[j*3]-=1
            

for _ in range(4):
    data=list(map(int,input().split()))
    print(f(data),end=" ")