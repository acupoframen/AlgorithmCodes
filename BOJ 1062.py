import sys
input = sys.stdin.readline
def dfs(start, cnt):
    global ans
    if cnt == k - 5:
        tmp = 0
        for word in words:
            is_contain = 1 
            for c in word:
                if not check[ord(c) - ord('a')]:    
                    is_contain = 0
                    break
            if is_contain:
                tmp += 1
        ans = max(ans, tmp)
        return
    for i in range(start, 26):
        if not check[i]:
            check[i] = 1
            dfs(i, cnt + 1)
            check[i] = 0
n, k = map(int, input().split())
words = [set(input().strip()) for _ in range(n)]
check = [0] * 26
ans = 0
if k < 5:
    print(0)   
    exit(0)
elif k == 26:
    print(n)  
    exit(0)
for c in ('a', 'c', 'i', 'n', 't'):
    check[ord(c) - ord('a')] = 1
dfs(0, 0)
print(ans)