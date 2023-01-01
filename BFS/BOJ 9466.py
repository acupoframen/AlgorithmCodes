t=int(input())
for _ in range(t):
    n=int(input())
    data=[0]+list(map(int,input().split()))
    visited=[False for _ in range(n+1)]
    res=0
    for i in range(1,n+1):
        if visited[i]:
            continue
        num=i
        q=[num]
        visited[num]=True
        while True:
            newnum=data[q[-1]]
            if visited[newnum]:
                if newnum in q:
                    visited[newnum]=True
                    res+=(len(q)-q.index(newnum))
                break
            else:
                q.append(newnum)
                visited[newnum]=True
    print(n-res)