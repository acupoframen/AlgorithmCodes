n=int(input())
data=list(map(int,input().split()))
answer=[]
for i in range(1,min(data)+1):
    flag=0
    for j in data:
        if j%i:
            flag=1
            break
    if not flag:
        answer.append(i)
for i in answer:
    print(i)