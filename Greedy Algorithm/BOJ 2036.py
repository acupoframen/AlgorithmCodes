n=int(input())
pos=[]
neg=[]
zero=0
one=0
for _ in range(n):
    num=int(input())
    if num>1:
        pos.append(num)
    elif num<0:
        neg.append(num)
    elif num==1:
        one+=1
    else:
        zero=1
    

pos.sort()
neg.sort(reverse=True)

answer=0
while pos:
    if len(pos)>=2:
        a=pos.pop()
        b=pos.pop()
        answer+=a*b
    else:
        answer+=pos.pop()

while neg:
    if len(neg)>=2:
        a=neg.pop()
        b=neg.pop()
        answer+=a*b
    else:
        if zero:
            break
        else:
            answer+=neg.pop()

answer+=one
print(answer)