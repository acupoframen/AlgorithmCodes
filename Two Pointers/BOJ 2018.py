n=int(input())
left=1
right=1
answer=0
curr=1
while left <= n:
    if curr == n:
        answer += 1
        curr -= left
        left += 1
    elif curr < n:
        right += 1
        curr += right
    else:
        curr -= left
        left += 1
print(answer)