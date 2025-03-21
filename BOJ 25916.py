n, m = map(int, input().split())  
data = list(map(int, input().split())) 

left = 0  
right = 0 
temp = 0  
answer = 0

while right < n:
    if temp > m:
        temp -= data[left]
        left += 1
    else:  
        answer = max(answer, temp)
        temp += data[right]
        right += 1

while left < right:
    if temp > m:
        temp -= data[left]
        left += 1
    else:
        answer = max(answer, temp)
        break

print(answer)
