from collections import defaultdict
n=int(input())
data=defaultdict(int)
temp=list(map(int,input().split()))
for i in range(n):
    num=temp[i]
    data[num]+=1
    while num%2==0:
        num//=2
        data[num]+=1
print(max(data.values()))