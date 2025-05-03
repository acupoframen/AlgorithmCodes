n, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

answer = 0
val = 0
left = 0
right = 0

while right < n:
    if data[right][0] - data[left][0] < d:
        val += data[right][1]
        answer = max(answer, val)
        right += 1
    else:
        val -= data[left][1]
        left += 1
print(answer)
