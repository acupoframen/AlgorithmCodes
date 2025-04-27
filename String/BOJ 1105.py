l, r = input().split()
if len(l) != len(r):
    print(0)
    exit(0)

cnt = 0
for l_digit, r_digit in zip(l, r):
    if l_digit != r_digit:
        break
    if l_digit == '8':
        cnt += 1
print(cnt)
