import sys
input=sys.stdin.readline
while True:
    num,*data=list(map(int,input().split()))
    if num==0:
        break
    data.append(0)
    stack=[]
    answer=0
    for i in range(len(data)):
        while len(stack) and data[stack[-1]]>data[i]:
            temp=stack.pop()
            if not len(stack):
                width=i
            else:
                width=i-stack[-1]-1
            answer=max(answer,width*data[temp])
        stack.append(i)
    print(answer)