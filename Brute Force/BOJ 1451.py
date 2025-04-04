def calc(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]

n, m = map(int, input().split())
data = [[0] * (m + 1)]
for _ in range(n):
    data.append([0] + list(map(int, list(input()))))

s = [[0] * (m + 1) for _ in range(n + 1)]
for row in range(1, n + 1):
    for col in range(1, m + 1):
        s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + data[row][col]

answer = 0

for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = calc(1, 1, n, i)
        r2 = calc(1, i+1, n, j)
        r3 = calc(1, j+1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3
 
 
# 두 번째 경우: 전체 직사각형을 가로로만 분할한 경우
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = calc(1, 1, i, m)
        r2 = calc(i+1, 1, j, m)
        r3 = calc(j+1, 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3
 
# 세 번째 경우: 전체 세로 분할 후 우측 가로 분할한 경우
for i in range(1, m):
    for j in range(1, n):
        r1 = calc(1, 1, n, i)
        r2 = calc(1, i+1, j, m)
        r3 = calc(j+1, i+1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3
 
# 네 번째 경우: 전체 세로 분할 후 좌측 가로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = calc(1, 1, i, j)
        r2 = calc(i+1, 1, n, j)
        r3 = calc(1, j+1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3
 
# 다섯번 째 경우: 전체 가로 분할 후 하단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = calc(1, 1, i, m)
        r2 = calc(i+1, 1, n, j)
        r3 = calc(i+1, j+1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3
 
# 여섯번 째 경우: 전체 가로 분할 후 상단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = calc(1, 1, i, j)
        r2 = calc(1, j+1, i, m)
        r3 = calc(i+1, 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3
print(answer)