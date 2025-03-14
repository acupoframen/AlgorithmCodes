import math
n, b = map(int, input().split())
sumx = 0
sumy = 0
for _ in range(n):
    x, y = map(int, input().split())
    sumx += x
    sumy += y
if sumx == 0:
    print("EZPZ")
    exit(0)

num = sumy - n * b
den = sumx

if num % den == 0:
    print(num // den)
else:
    if den < 0:
        num, den = -num, -den
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    print(f"{num}/{den}")
