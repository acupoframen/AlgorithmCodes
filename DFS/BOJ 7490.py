import sys
input = sys.stdin.readline

def dfs(n, idx, rst):
    if idx == n:
        ans = eval(rst.replace(' ', ''))
        if ans == 0:
            answer.append(rst)
        return
    else:        
        dfs(n, idx+1, rst + ' ' + str(idx+1))
        dfs(n, idx+1, rst + '+' + str(idx+1))
        dfs(n, idx+1, rst + '-' + str(idx+1))

t = int(input())
for _ in range(t):
    n = int(input())
    answer = []
    dfs(n, 1, '1')
    for a in answer:
        print(a)
    print()