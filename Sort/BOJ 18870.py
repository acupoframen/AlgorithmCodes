n=int(input())
data=list(map(int,input().split()))
temp=list(sorted(set(data)))

answer={}
num=0
for i in temp:
    answer[i]=num
    num+=1

for i in range(n):
    data[i]=answer[data[i]]

print(*data)