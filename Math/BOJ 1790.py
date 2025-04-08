import sys
n, k = map(int, sys.stdin.readline().split())
ans = 0
num = 1
nine = 9
while k > num * nine:
    k -= (num * nine)
    ans += nine 
    num += 1
    nine = nine * 10

ans = (ans+1) + (k-1) // num

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1) % num])