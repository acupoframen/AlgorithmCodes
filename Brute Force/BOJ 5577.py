import sys
sys.setrecursionlimit(10000)  
INF = int(1e9)

def rby_pang(ball, down, up, left):
    n = len(ball)
    successive_down = 1
    successive_up = 1
    next_down = down
    next_up = up

    while next_up + 1 < n and ball[next_up] == ball[next_up + 1]:
        next_up += 1
        successive_up += 1

    while next_down - 1 >= 0 and ball[next_down] == ball[next_down - 1]:
        next_down -= 1
        successive_down += 1

    if ball[down] == ball[up]:
        if down == up:
            max_successive = successive_down + successive_up - 1
        else:
            max_successive = successive_down + successive_up
    else:
        max_successive = max(successive_down, successive_up)

    if max_successive >= 4:
        if left - max_successive < 4:
            return left - max_successive

        if next_down == 0:
            next_down = next_up
        else:
            next_down -= 1

        if next_up == n - 1:
            next_up = next_down
        else:
            next_up += 1

        new_ball = ball[:next_down+1] + ball[next_up:]
        return rby_pang(new_ball, next_down, next_up - (next_up - next_down - 1), left - max_successive)
    else:
        return left

n = int(sys.stdin.readline())
ball = [int(sys.stdin.readline()) for _ in range(n)]

answer = INF
for i in range(n):
    cur = ball[i]
    m = INF
    for color in [1, 2, 3]:
        if color == cur:
            continue
        new_ball = ball[:]
        new_ball[i] = color
        m = min(m, rby_pang(new_ball, i, i, n))
    answer = min(answer, m)

print(answer)
