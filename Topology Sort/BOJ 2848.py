import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

edge = [set() for _ in range(26)]
alpha = set()
n = int(input())
data = [input() for _ in range(n)]
indegree = [0] * 26
for i in range(n - 1):
    for x, y in zip(data[i], data[i + 1]):
        if x != y:
            x = ord(x) - ord('a')
            y = ord(y) - ord('a')
            if y not in edge[x]:
                edge[x].add(y)
                indegree[y] += 1
            break
    else:
        if len(data[i]) > len(data[i + 1]):
            print('!')
            quit()
for word in data:
    for ch in word:
        alpha.add(ord(ch) - ord('a'))

q = []
for i in alpha:
    if indegree[i] == 0:
        heapq.heappush(q, i)

ambiguous = False
ans = []
while q:
    if len(q) > 1:
        ambiguous = True
    a = heapq.heappop(q)
    ans.append(a)
    for nxt in edge[a]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(q, nxt)

if len(ans) != len(alpha):
    print('!')
else:
    if ambiguous:
        print('?')
    else:
        print("".join(map(lambda x: chr(x + ord('a')), ans)))
