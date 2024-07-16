from collections import deque
n=int(input())
for _ in range(n):
    d=input()
    stack=deque()
    answer=deque()
    for i in d:
        if i=='<':
            if len(answer):
                stack.append(answer.pop())
        elif i=='>':
            if len(stack):
                answer.append(stack.pop())
        elif i=='-':
            if len(answer):
                answer.pop()
        else:
            answer.append(i)
    while stack:
        answer.append(stack.pop())
    print("".join(answer))