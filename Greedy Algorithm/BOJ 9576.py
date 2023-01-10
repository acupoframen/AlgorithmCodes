import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(m)]
    data.sort(key = lambda x: (x[1],x[0]))
    answer=0
    visited=[False]*(n+1)
    for a,b in data:
        for i in range(a,b+1):
            if not visited[i]:
                visited[i]=True
                answer+=1
                break
    print(answer)