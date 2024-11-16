n=int(input())
data=input()
answer=0
lcount=0
scount=0
for i in range(n):
    if ord('1')<=ord(data[i])<=ord('9'):
        answer+=1
    elif data[i]=='L':
        lcount+=1
    elif data[i]=='R':
        if lcount>0:
            lcount-=1
            answer+=1
        else:
            break
    elif data[i]=='S':
        scount+=1
    else:
        if scount>0:
            scount-=1
            answer+=1
        else:
            break
print(answer)