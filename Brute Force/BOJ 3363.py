data=list()
for _ in range(3):
    a=input()
    if a:
        a=list(a.split())
        data.append(a)
answer=[]
for i in range(12):
    flag=0
    for j in range(3):
        if data[j][4]=='>':
            if str(i) in data[j][:4]:
                continue
            else:
                flag=1
                break
        elif data[j][4]=='<':
            if str(i) in data[j][5:]:
                continue
            else:
                flag=1
                break
        else:
            if str(i) in data[j]:
                flag=1
                break
    if not flag:
        answer.append(str(i)+"+")

for i in range(12):
    flag=0
    for j in range(3):
        if data[j][4]=='<':
            if str(i) in data[j][:4]:
                continue
            else:
                flag=1
                break
        elif data[j][4]=='>':
            if str(i) in data[j][5:]:
                continue
            else:
                flag=1
                break
        else:
            if str(i) in data[j]:
                flag=1
                break
    if not flag:
        answer.append(str(i)+"-")

if len(answer)==0:
    print("impossible")
elif len(answer)==1:
    print(answer[0])
else:
    print("indefinite")