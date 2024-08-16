from collections import defaultdict
n=input()
d=defaultdict(int)
for i in range(1,len(n)+1):
    for j in range(len(n)-i+1):
        d[n[j:j+i]]=1
print(len(d))