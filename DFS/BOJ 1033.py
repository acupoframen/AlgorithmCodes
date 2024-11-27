import sys
n=int(input())
data = [[] for _ in range(n)]
lcm = 1
def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)
for _ in range(n - 1):
    a, b, p, q = map(int,input().split())
    data[a].append([b, p, q])
    data[b].append([a, q, p])
    lcm *= (p * q // gcd(p, q))
visited = [True] * n
def DFS(v):
    visited[v] = False
    for i in data[v]:
        if visited[i[0]]:
            answer[i[0]] = answer[v] * i[2] // i[1]
            DFS(i[0])
answer = [0] * n
answer[0] = lcm
DFS(0)
gcdval = answer[0]
for i in range(1, n):
    gcdval = gcd(gcdval, answer[i])
for i in range(n):
    print(int(answer[i] // gcdval), end=' ')