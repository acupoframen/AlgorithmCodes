import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
diff = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    diff[a] += 1
    diff[b] -= 1

removed = 0
current = 0

for i in range(1, n):
    current += diff[i]
    if current > 0:
        removed += 1

print(n - removed)