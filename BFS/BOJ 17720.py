from collections import deque
n,m=map(int,input().split())
data=list([] for _ in range(n))
received=list(0 for _ in range(n))
for _ in range(m):
    a,b=input().split()
    a=ord(a)-ord('A')
    b=ord(b)-ord('A')
    data[a].append(b)
    received[b]+=1
st=received.index(0)
visited=list(0 for _ in range(n))
infos=list(map(lambda x: ord(x)-ord('A'),input().split()[1:]))
q=deque()
for i in range(n):
    if received[i] == 0 and i not in infos:
        q.append(i)
        visited[i] = True
while q:
    curr=q.popleft()
    for i in data[curr]:
        if i not in infos and not visited[i]:
            q.append(i)
            visited[i]=1
print(sum(1 for i in range(n) if visited[i] and received[i] != 0))