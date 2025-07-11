from collections import deque
import sys
input=  sys.stdin.readline
while True:
    n= int(input())
    if n == 0:
        break
    data=[1e10]
    for _ in range(n):
        t,money,*next=input().split()
        next=list(map(int,next))
        data.append([t,int(money),next[:-1]])
    visited=list(-1 for _ in range(n+1))
    flag=0
    q=deque()
    if data[1][0]== 'T':
        print('No')
        continue
    elif data[1][0]=='L':
        q.append((1,data[1][1]))
        visited[1]=data[1][1]
    else:
        q.append((1,0))
        visited[1]=0
    while q:
        curr,money=q.popleft()
        if curr == n:
            flag=1
            break
        for next in data[curr][2]:
            if data[next][0]=='T':
                if data[next][1]>money:
                    continue
                nextmoney=money-data[next][1]
            elif data[next][0]=='L':
                nextmoney=max(money,data[next][1])
            else:
                nextmoney=money
            if visited[next]<nextmoney:
                visited[next]=nextmoney
                q.append([next,nextmoney])
    if flag:
        print('Yes')
    else:
        print('No')