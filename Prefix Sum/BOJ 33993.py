n,r,c,w = map(int, input().split())
data = [[0] * (c+1) for _ in range(r+1)]

for _ in range(n):
    x,y= map(int, input().split())
    data[x][y]=1  
dp = [[0] * (c + 1) for _ in range(r + 1)]
for i in range(1, r + 1):
    for j in range(1, c + 1):
        dp[i][j] = dp[i - 1][j]+ dp[i][j - 1]- dp[i - 1][j - 1]+ data[i][j]

def func(x1, y1, x2, y2):
    x1 = max(1, x1)
    y1 = max(1, y1)
    x2 = min(r, x2)
    y2 = min(c, y2)
    return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]

offset = w // 2
answer = -1
result = (r + 1, c + 1)  

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if data[i][j]: 
            continue
        cnt = func(i - offset, j - offset, i + offset, j + offset)
        if cnt > answer:
            answer = cnt
            result = (i, j)
        elif cnt == answer:
            result = min(result, (i, j)) 

print(answer)
print(result[0], result[1])
