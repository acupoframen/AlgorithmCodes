from collections import defaultdict
n = int(input())
data = [input().strip() for _ in range(n)]
first = defaultdict(int)
for char in data[0]:
    first[char] += 1
answer = 0
for word in data[1:]:
    temp = defaultdict(int)
    for char in word:
        temp[char] += 1
    diff_add = 0
    diff_remove = 0
    for j in range(26):
        char = chr(j + ord('A'))
        diff = temp[char] - first[char]
        if diff > 0:
            diff_add+=diff
        elif diff < 0:
            diff_remove-=diff
    length_diff = abs(len(word) - len(data[0]))
    if length_diff == 0 and (diff_add == 1 and diff_remove == 1 or diff_add == 0 and diff_remove == 0):
        answer += 1
    elif length_diff == 1 and (diff_add == 1 and diff_remove == 0 or diff_add == 0 and diff_remove == 1):
        answer += 1

print(answer)