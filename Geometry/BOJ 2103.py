import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
vx = defaultdict(list)
vy = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    vx[x].append(y)
    vy[y].append(x)

ans = 0
for i in range(10001):
    if vx[i]:
        vx[i].sort()
        for j in range(0, len(vx[i]), 2):
            ans += vx[i][j+1] - vx[i][j]
    if vy[i]:
        vy[i].sort()
        for j in range(0, len(vy[i]), 2):
            ans += vy[i][j+1] - vy[i][j]

print(ans)
