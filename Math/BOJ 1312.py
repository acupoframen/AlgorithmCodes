a, b, k = map(int, input().split())
remainder = a % b
for _ in range(k - 1):
    remainder = (remainder * 10) % b
answer = (remainder * 10) // b
print(answer)