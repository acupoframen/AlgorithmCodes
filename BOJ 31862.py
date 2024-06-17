import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
notfinished=[]
standing=[0 for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if c==0:
        notfinished.append([a,b])
    elif c==1:
        standing[a]+=1
    else:
        standing[b]+=1
answer=0
def dfs(idx,currstanding):
    global answer,k
    if idx==len(notfinished):
        max_score = max(standing)
        if standing[k] == max_score and standing.count(max_score) == 1:
            answer += 1
        return
    a,b=notfinished[idx]
    currstanding[a]+=1
    dfs(idx+1,currstanding)
    currstanding[a]-=1
    currstanding[b]+=1
    dfs(idx+1,currstanding)
    return
dfs(0,standing)
print(answer)