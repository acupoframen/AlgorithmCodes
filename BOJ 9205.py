from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    home=list(map(int,input().split()))
    cvcoord=list(list(map(int,input().split())) for _ in range(n))
    cvvisited=list(0 for _ in range(n))
    goal=list(map(int,input().split()))
    q=deque()
    q.append(home)
    answer=0
    while q:
        x,y=q.popleft()
        if abs(x-goal[0])+abs(y-goal[1])<=1000:
            answer=1
            break
        for i in range(n):
            nx,ny=cvcoord[i][0],cvcoord[i][1]
            if abs(nx-x)+abs(ny-y)<=1000 and not cvvisited[i]:
                q.append([nx,ny])
                cvvisited[i]=1
    if answer:
        print("happy")
    else:
        print("sad")