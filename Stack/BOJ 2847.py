n=int(input())
data=list(int(input()) for _ in range(n))
answer=0
stack=[]
for i in range(n-1,-1,-1):
    if not stack:
        stack.append(data[i])
        continue
    if data[i]>=stack[-1]:
        answer+=(data[i]-stack[-1]+1)
        stack.append(stack[-1]-1)
    else:
        stack.append(data[i])
print(answer)