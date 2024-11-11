from collections import defaultdict
n=int(input())
d=defaultdict(int)
data=set()
for i in range(n):
    a,b=input().split('.')
    data.add(b)
    d[b]+=1
data=sorted(list(data))
for i in range(len(data)):
    print(data[i],d[data[i]])