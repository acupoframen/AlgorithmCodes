n,m=map(int,input().split())
data=[[0]*(m+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]
answer=0
dx=[[-1,0],[1,0],[0,1],[0,-1]]

for i in range(1,n+1):
    for j in range(1,m+1):
        minVal=1e10
        for a,b in dx:
            minVal=min(minVal,data[i+a][j+b])
        if not data[i][j]:
            continue
        if data[i][j]>minVal:
            answer+=minVal
        else:
            answer+=(data[i][j]-1)
print(answer)