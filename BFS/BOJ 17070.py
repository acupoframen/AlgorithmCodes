from collections import deque
n=int(input())
data=[[0 for _ in range(n+1)]]+list([0]+list(map(int,input().split())) for _ in range(n))

answer=0

q=deque()
q.append([1,2,'r'])
while q:
    x,y,direction=q.pop()
    if x==n and y==n:
        answer+=1
        continue
    if  direction=="r":
        if y+1<=n and not data[x][y+1]:
            q.append([x,y+1,"r"])
        if x+1<=n and y+1<=n and not sum(data[x][y:y+2])+sum(data[x+1][y:y+2]):
            q.append([x+1,y+1,"rd"])
    elif direction=="rd":
        if y+1<=n and not data[x][y+1]:
            q.append([x,y+1,"r"])
        if x+1<=n and y+1<=n and not sum(data[x][y:y+2])+sum(data[x+1][y:y+2]):
            q.append([x+1,y+1,"rd"])
        if x+1<=n and not data[x+1][y]:
            q.append([x+1,y,"d"])
    else:
        if x+1<=n and y+1<=n and not sum(data[x][y:y+2])+sum(data[x+1][y:y+2]):
            q.append([x+1,y+1,"rd"])
        if x+1<=n and not data[x+1][y]:
            q.append([x+1,y,"d"])
print(answer)
