import sys
from collections import deque

def bfs():
    q=deque()
    q.append(n)
    while q:
        num=q.popleft()
        if num==k:
            print(loc[k])
            break
        for i in (num-1,num+1,num*2):
            if 0<=i<=200000 and loc[i]==0:
                loc[i]=loc[num]+1
                q.append(i)
                
loc=[0]*200001
n,k=map(int,input().split())

bfs()
