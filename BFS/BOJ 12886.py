from collections import deque
a,b,c=map(int,input().split())
total=a+b+c
if not total%3:
    visited=list(list(0 for _ in range(total+1)) for _ in range(total+1))
    q=deque([[a,b]])
    visited[a][b]=1
    while q:
        a,b=q.popleft()
        c=total-a-b
        if a==b==c:
            print(1)
            exit(0)
        for x,y in [[a,b],[b,c],[a,c]]:
            if x==y:
                continue
            if x>y:
                x,y=y,x
            x,y=x+x,y-x
            minval=min(x,y,total-x-y)
            maxval=max(x,y,total-x-y)
            if visited[minval][maxval]:
                continue
            q.append([minval,maxval])
            visited[minval][maxval]=1
    print(0)
else:
    print(0)