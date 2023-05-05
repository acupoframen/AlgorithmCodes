r,c=map(int,input().split())
data=[]
for _ in range(r):
    data.append(list(input()))
alphabet=set()
alphabet.add(data[0][0])
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,num):
    global answer
    answer=max(num,answer)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and data[nx][ny] not in alphabet:
            alphabet.add(data[nx][ny])
            dfs(nx,ny,num+1)
            alphabet.remove(data[nx][ny])
answer=1
dfs(0,0,answer)
print(answer)