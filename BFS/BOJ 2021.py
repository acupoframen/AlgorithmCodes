from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
stations = [[] for _ in range(n+1)]
lines = []

for i in range(l):
    temp = list(map(int, input().split()))[:-1]
    for j in temp:
        stations[j].append(i)
    lines.append(temp)

q = deque()
visited_line = [0 for _ in range(l)]

start, end = map(int, input().split())

for i in stations[start]:
    for k in lines[i]:
        q.append((0, k))
        visited_line[i] = 1
        if k == end:
            print(0)
            exit(0)

while q:
    depth, st = q.popleft()
    for k in stations[st]:
        if visited_line[k]:
            continue
        visited_line[k] = 1
        for j in lines[k]:
            if j == end:
                print(depth + 1)
                exit(0)
            q.append((depth + 1, j))

print(-1)
