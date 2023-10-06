n,m=map(int,input().split())
answer=[]
data={}
for _ in range(n):
    name=input()
    data[name]=1
for _ in range(m):
    name=input()
    if name in data:
        answer.append(name)

print(len(answer))
for i in (sorted(answer)):
    print(i)