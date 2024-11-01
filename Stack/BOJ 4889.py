game=1
while True:
    stack=[]
    n=input()
    answer=0
    if '-' in n:
        break
    for i in n:
        if i == "{":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                answer+=1
                stack.append('{')
    
    answer+= len(stack)//2
        
    print(f'{game}. {answer}')
    game+=1