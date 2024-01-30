import sys
def build_kmp_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j

    return table

def kmp_search(text, pattern):
    count = 0
    ans = []
    m, n = len(pattern), len(text)
    kmp_table = build_kmp_table(pattern)
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = kmp_table[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            count += 1
            ans.append(i - m + 2)
            j = kmp_table[j - 1]

    return count, ans

t = input()
p = input()

if len(t) < len(p):
    print(0)
else:
    count, ans = kmp_search(t, p)
    print(count)
    print(*ans)
