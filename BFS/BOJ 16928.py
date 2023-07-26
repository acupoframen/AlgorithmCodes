from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
ladders=[1e10 for _ in range(101)]
snakes=[1e10 for _ in range(101)]
counts=[1e10 for _ in range(101)]
for _ in range(n):
    a,b=map(int,input().split())
    ladders[a]=b

for _ in range(m):
    a,b=map(int,input().split())
    snakes[a]=b

q=deque()
q.append(1)
counts[1]=0
while q:
    num=q.popleft()
    if num==100:
        print(counts[num]+1)
        exit()
    for i in range(1,7):
        if num+i>100:
            break
        if num+i==100:
            print(counts[num]+1)
            exit()
        
        if ladders[num+i]!=1e10:
            if counts[ladders[num+i]]>counts[num]+1:
                q.append(ladders[num+i])
                counts[ladders[num+i]]=counts[num]+1
        elif snakes[num+i]!=1e10:
            if counts[snakes[num+i]]>counts[num]+1:
                q.append(snakes[num+i])
                counts[snakes[num+i]]=counts[num]+1
        elif counts[num+i]>counts[num]+1:
            counts[num+i]=counts[num]+1
            q.append(num+i)