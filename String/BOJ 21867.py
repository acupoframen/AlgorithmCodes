n=int(input())
answer=[]
data=list(input())
for i in range(n):
    if data[i] not in ['J','A','V']:
        answer.append(data[i])

if len(answer)==0:
    print("nojava")
else:
    print("".join(answer))