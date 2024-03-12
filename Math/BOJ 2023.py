import math
def prime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return 0
    return 1

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10, 2):
            tmp = num * 10 + i
            if prime(tmp):
                dfs(tmp)
n = int(input())
for i in [2, 3, 5, 7]:
    dfs(i)