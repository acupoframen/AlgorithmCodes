n=input()
answer=0
data=n.split('-')
for i in data[0].split('+'):
    answer+=int(i)
for i in data[1:]:
    for j in i.split('+'):
        answer-=int(j)

print(answer)