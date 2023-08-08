import sys
input=sys.stdin.readline
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
N, K = map(int, input().split())
data= [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
record = [[[] for _ in range(N)] for _ in range(N)]

horses_info = [[] for _ in range(K + 1)]
for i in range(1, K + 1):
    r, c, direction = map(int, sys.stdin.readline().rstrip().split())
    horses_info[i] = [i, r - 1, c - 1, direction]
    record[r - 1][c - 1].append(i)


def is_bottom_horse(h_num, x, y):
    horse_state = record[x][y]
    if horse_state[0] == h_num:
        return True
    else:
        return False

def reverse_dir(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3


def is_blue_again(x, y, direction):
    rev_dir = reverse_dir(direction)
    nnx = x + dx[rev_dir]
    nny = y + dy[rev_dir]

    if nnx < 0 or nny < 0 or nnx >= N or nny >= N or data[nnx][nny] == 2:
        return True
    return False
def move_next_pos(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or nx >= N or ny >= N or data[nx][ny] == 2:
        if is_blue_again(x, y, direction):
            return x, y, reverse_dir(direction)
        else:
            rev_dir = reverse_dir(direction)
            return move_next_pos(x, y, rev_dir)
    elif data[nx][ny] == 1:
        rev_horses = record[x][y][::-1]
        for value in rev_horses:
            record[nx][ny].append(value)
            h_n, x, y, d = horses_info[value]
            horses_info[value] = [h_n, nx, ny, d]
        record[x][y] = []
    elif data[nx][ny] == 0:
        for value in record[x][y]:
            record[nx][ny].append(value)
            h_n, x, y, d = horses_info[value]
            horses_info[value] = [h_n, nx, ny, d]
        record[x][y] = []

    return nx, ny, direction
def move_all_horses():
    for horse in range(1, K + 1):
        horse_num, r, c, direction = horses_info[horse]
        if not is_bottom_horse(horse_num, r, c):
            continue
        nx, ny, n_dir = move_next_pos(r, c, direction)
        horses_info[horse_num] = [horse_num, nx, ny, n_dir]
def is_finish():
    for i in range(N):
        for j in range(N):
            if len(record[i][j]) >= 4:
                return True
    return False

answer = -1
time = 1
while time <= 1000:
    move_all_horses()

    if is_finish():
        answer = time
        break

    time += 1

print(answer)