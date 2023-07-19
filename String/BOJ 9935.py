data=input()
bomb=input()

stack=[]
for i in data:
    stack.append(i)
    if i==bomb[-1] and bomb=="".join(stack[-len(bomb):]):
        
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")

