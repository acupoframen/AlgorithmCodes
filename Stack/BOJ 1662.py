s=list(input())
stack=[]
length=0
multiple=0
for i in s:
    if i=="(":
        stack.append([length-1,multiple])
        length=0
    elif i==")":
        templength,tempmultiple=stack.pop()
        length=length*tempmultiple+templength
    else:
        length+=1
        multiple=int(i)
print(length)