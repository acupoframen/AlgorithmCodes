import sys
input = sys.stdin.readline
from itertools import permutations

n, m, q = map(int, input().split())

def find(a, data):
    if data[a] != a:
        data[a] = find(data[a], data)
    return data[a]

def union(a, b, data):
    a = find(a, data)
    b = find(b, data)
    if a < b:
        data[b] = a
    else:
        data[a] = b

data = [[] for _ in range(5)]

for _ in range(m):
    a, b, c = input().split()
    data[ord(c) - ord("A")].append([int(a), int(b)])

possibilities = {}

for perm in permutations([0, 1, 2, 3, 4]):
    parents = [i for i in range(n + 1)]
    templist = [0 for _ in range(5)]
    for uni in perm:
        for a, b in data[uni]:
            if find(a, parents) != find(b, parents):
                union(a, b, parents)
                templist[uni] += 1
    possibilities[perm] = tuple(templist)
    
for _ in range(q):
    answer = 0
    values = list(map(int, input().split()))
    temp = sorted(range(5), key=lambda k: values[k])
    templist = possibilities[tuple(temp)]  
    for i in range(5):
        answer += templist[i] * values[i]
    print(answer)
