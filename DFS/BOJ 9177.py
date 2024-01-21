import sys
from collections import deque
input= sys.stdin.readline

n=int(input())
for i in range(1,n+1):
    data=list(input().split())
    q=deque()
    q.append(data)
    visited=[[0 for _ in range(len(data[1])+1)] for _ in range(len(data[0])+1)]
    flag=1
    while q:
        a,b,c=q.popleft()
        if a=="" and b=="" and c=="":
            print(f"Data set {i}: yes")
            flag=0
            break

        elif c=="":
            break
        if len(a)>0 and a[0]==c[0] and visited[len(a)-1][len(b)]==0:
            visited[len(a)-1][len(b)]=1
            q.append([a[1:],b,c[1:]])
        if len(b)>0 and b[0]==c[0] and visited[len(a)][len(b)-1]==0:
            visited[len(a)][len(b)-1]=1
            q.append([a,b[1:],c[1:]])
    if flag:
        print(f"Data set {i}: no")