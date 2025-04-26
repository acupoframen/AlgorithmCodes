n=input()
stack=[]
for i in range(len(n)):
    stack.append(n[i])
    while len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("P")

if stack == ['P']:
    print("PPAP")
else:
    print("NP")