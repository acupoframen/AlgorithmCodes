N = int(input())
number = [] 
ans = [0] * N
maxValue = -1
for i in range(N):
    number.append(int(input()))
    if number[i] > maxValue:
        maxValue = number[i]
cnt = [0] * (maxValue+1)
for i in number:
    cnt[i] += 1
for i in range(N):
    value = 1
    while value*value <= number[i]:
        if number[i] % value == 0:
            if value*value != number[i]:
                ans[i] += cnt[value] + cnt[number[i]//value]
            else:
                ans[i] += cnt[value]
        value += 1
for res in ans:
    print(res-1) 