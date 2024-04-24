import sys
input=sys.stdin.readline
try:
    n=int(input())
    data=[list() for _ in range(n+1)]
    linelist=[[0]]
    for _ in range(n-1):
        a,b=map(int,input().split())
        data[a].append(b)
        data[b].append(a)
        linelist.append([a,b])
    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split())
        if a==1:
            if len(data[b])==1:
                print("no")
            else:
                print("yes")
        else:
            print("yes")
except:
    exit(0)