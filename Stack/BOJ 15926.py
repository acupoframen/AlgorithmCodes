n=int(input())
data=list(input())
answer=0
count=[0 for _ in range(n)]
stack=[]
temp=0
for i in range(n):
    if data[i]=='(':
        stack.append(i)
    else:
        if stack:
            count[i]=count[stack[-1]]=1
            stack.pop()
for i in count:
    if i==1:
        temp+=1
        answer=max(answer,temp)
    else:
        temp=0
print(answer)