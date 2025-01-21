from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = 0
for i in range(len(data)-2):
    left, right = i+1, n-1
    while left < right:
        result = data[i]+data[left]+data[right]
        if result > 0:
            right -= 1
        else:
            if result == 0:
                if data[left] == data[right]:
                    answer += right - left
                else:
                    idx = bisect_left(data, data[right])
                    answer += right-idx+1
            left += 1

print(answer)