n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split()))[:-1])

for i in range(1,2**31+1):
    temp=[]
    for j in range(n):
        temp.append(str(data[j][:i]))
    if len(set(temp))==n:
        print(i)
        exit(0)
