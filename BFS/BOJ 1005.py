from collections import deque
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    time=[0]+list(map(int,input().split()))
    adj=[[] for _ in range(n+1)]
    degree=[0]*(n+1)
    answer=[0]*(n+1)
    for _ in range(k):
        a,b=map(int,input().split())
        adj[a].append(b)
        degree[b]+=1
    w=int(input())
    q=deque()
    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)
            answer[i]=time[i]
    while q:
        a=q.popleft()
        if a==w:
            break
        for b in adj[a]:
            answer[b]=max(answer[b], answer[a]+time[b])
            if degree[b]==1:
                q.append(b)
            degree[b]-=1
    print(answer[w])