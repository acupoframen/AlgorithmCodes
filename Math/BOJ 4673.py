data=[]
for i in range(1,10001):
    temp=0
    for j in str(i):
        temp+=int(j)
    data.append(i+temp)

answer=[]
for i in range(1,10001):
    if not i in data:
        answer.append(i)
for i in answer:
    print(i)