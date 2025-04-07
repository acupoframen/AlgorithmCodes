import sys
input = sys.stdin.readline
def floyd_warshall(n, data):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if data[i][j] > data[i][k] + data[k][j]:
                    data[i][j] = data[i][k] + data[k][j]
def dfs(cur, visited, cost):
    global answer
    if visited == (1 << n) - 1:
        answer = min(answer, cost)
        return

    for nxt in range(n):
        if not (visited & (1 << nxt)):
            dfs(nxt, visited | (1 << nxt), cost + data[cur][nxt])

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

floyd_warshall(n, data)

answer = float('inf')
dfs(k, 1 << k, 0)

print(answer)
