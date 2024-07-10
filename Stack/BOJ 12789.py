n = int(input())
data = list(map(int, input().split()))
stack = []
target = 1
while data:
    if data[0] == target:
        data.pop(0)
        target += 1
    else:
        stack.append(data.pop(0))
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
if not stack: 
    print('Nice')
else:
    print('Sad')