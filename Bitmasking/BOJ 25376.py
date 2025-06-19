from collections import deque
n = int(input())
s = 0
chng = [0] * 20
dist = [-1] * (1 << 20)
x_list = list(map(int, input().split()))
for i in range(n):
    if x_list[i]:
        s |= (1 << i)
        
for i in range(n):
    parts = list(map(int, input().split()))
    k = parts[0]
    chng[i] |= (1 << i)
    for j in range(1, k + 1):
        x = parts[j] - 1
        chng[i] |= (1 << x)

q = deque()
q.append(s)
dist[s] = 0

while q:
    cur = q.popleft()
    for i in range(n):
        if cur & (1 << i):  
            continue
        nxt = cur ^ chng[i]
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

print(dist[(1 << n) - 1])
