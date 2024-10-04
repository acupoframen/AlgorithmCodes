from collections import deque
st=input()
stack=deque()
answer=0
temp=1
for i in range(len(st)):
    if st[i]=='(':
        stack.append("(")
        temp*=2
    elif st[i]=='[':
        stack.append("[")
        temp*=3
    elif st[i]==')':
        if not stack or stack[-1]=='[':
            answer=0
            break
        if st[i-1]=='(':
            answer+=temp
        temp//=2
        stack.pop()
    else:
        if not stack or stack[-1]=='(':
            answer=0
            break
        if st[i-1]=='[':
            answer+=temp
        temp//=3
        stack.pop()



if stack:
    print(0)
else:
    print(answer)