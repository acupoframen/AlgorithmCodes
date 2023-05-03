import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
answer=[]
for i in range(n):
    q=deque([i])
    check=[0 for _ in range(n)]
    while q:
        x=q.popleft()
        for i in range(n):
            if data[x][i]==1 and check[i]==0:
                q.append(i)
                check[i]=1
    for j in range(n):
        print(check[j], end=' ')
    print()