n,m=map(int,input().split())
data={}
for i in range(n):
    name=input()
    count=int(input())
    data[name]=[]
    for j in range(count):
        data[name].append(input())
    data[name].sort()

for i in range(m):
    
    name=input()
    num=int(input())
    if num==0:
        for j in data[name]:
            print(j)
    else:
        for i in data.keys():
            if name in data[i]:
                print(i)
                break