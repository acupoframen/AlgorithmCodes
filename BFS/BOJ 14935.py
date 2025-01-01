from collections import deque
s,t=map(int,input().split())

q=deque()
q.append([s,''])
visited=set()
visited.add(s)

def f(num,op,newop):
    if 0<=num<=1e9 and num not in visited:
        q.append([num,op+newop])
        visited.add(num)
if s==t:
    print(0)
    exit(0)
while q:
    s,op=q.popleft()
    if s==t:
        print(op)
        exit(0)
    f(s*s,op,'*')
    f(s+s,op,'+')
    f(1,op,'/')
print(-1)