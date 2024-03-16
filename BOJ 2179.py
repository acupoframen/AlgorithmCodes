n=int(input())
data=list(input() for _ in range(n))
temp1=sorted(list(enumerate(data)),key= lambda x: x[1])

answer=0
s=20001
t=20001
for i in range(n-1):
    temp=0
    a,b=temp1[i][1],temp1[i+1][1]
    c,d=temp1[i][0],temp1[i+1][0]
    if temp1[i][0]>temp1[i+1][0]:
        c,d=temp1[i+1][0],temp1[i][0]
    for i in range(min(len(a),len(b))):
        if a[i]==b[i]:
            temp+=1
        else:
            break
    if answer<temp:
        answer=temp
        s=c
        t=d
    elif answer==temp:
        if s<c:
            continue
        elif s==c:
            if t<d:
                continue
            else:
                s,t=c,d
                continue
        else:
            s,t=c,d
    else:
        continue

for i in range(n):
    if temp1[i][0]==s:
        continue
    if len(temp1[i][1])>=answer and data[s][:answer]==temp1[i][1][:answer] and temp1[i][0]<=t:
        t=temp1[i][0]

print(data[s])
print(data[t])