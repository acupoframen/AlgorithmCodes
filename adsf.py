from collections import deque
import sys
sys.setrecursionlimit(int(1e5)+1)
n=int(input())
data=list(list() for _ in range(n+1))
for i in range(n-1):
    x,y=map(int,input().split())
    data[x].append(y)
    data[y].append(x)
tree=list(list() for _ in range(n+1))

q=deque()
q.append(1)
visited=list(0 for _ in range(n+1))
visited[1]=1

while q:
    node=q.popleft()
    for i in data[node]:
        if not visited[i]:
            visited[i]=1
            q.append(i)
            tree[node].append(i)

def play(curr,a,b,turn):
    temp=0
    if tree[curr]:
        for i in tree[curr]:
            if turn==0:
                #내 턴이면, 내가 이기는 경우를 고름
                if play(i,a+curr,b,1):
                    temp=1
            else:
                #상대 턴이면, 내가 지는 경우를 고름
                if not play(i,a,b+curr,0):
                    temp=0
                    break
                else:
                    temp=1
        return temp
    else:
        if turn==0:
            if a+curr>=b:
                return 1
            else:
                return 0
        else:
            if a>=b+curr:
                return 1
            else:
                return 0

for i in range(1,n+1):
    if play(i,0,0,0):
        print(1)
    else:
        print(0)