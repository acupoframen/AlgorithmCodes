while True:
    stri=input()
    if stri=='.':
        break
    stack=[]
    noflag=0
    for i in stri:
        if i=='[':
            stack.append('[')
        elif i=='(':
            stack.append('(')
        elif i==']':
            if len(stack)>=1 and stack[-1]=='[':
                del stack[-1]
            else:
                noflag=1
                break
        elif i==')':
            if len(stack)>=1 and stack[-1]=='(':
                del stack[-1]
            else:
                noflag=1
                break
    if noflag==1:
        print("no")
    elif len(stack)>0:
        print("no")
    else:
        print("yes")