data={}
n=int(input())
for _ in range(n):
    a,b=input().split()
    if b=="enter":
        data[a]=1
    else:
        data[a]=0
answer=[]
for i in data:
    if data[i]==1:
        answer.append(i)
answer.sort(reverse=True)
for i in answer:
    print(i)