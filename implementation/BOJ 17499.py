import sys
input = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))

num = 0  
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        index = (query[1] - 1 + num) % n  
        data[index] += query[2]
    elif query[0] == 2:
        num = (num - query[1]) % n
    elif query[0] == 3:
        num = (num + query[1]) % n
result = data[num:] + data[:num]
print(*result)
