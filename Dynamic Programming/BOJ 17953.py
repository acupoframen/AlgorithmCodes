n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * (n + 1) for _ in range(m)]
for i in range(m):
    dp[i][1] = data[i][0]

for j in range(2, n + 1):
    for i in range(m):
        for k in range(m):
            if i == k:
                dp[i][j] = max(dp[i][j], dp[k][j - 1] + data[i][j - 1] // 2)
            else:
                dp[i][j] = max(dp[i][j], dp[k][j - 1] + data[i][j - 1])

answer = 0
for i in range(m):
    answer = max(answer, dp[i][n])

print(answer)
