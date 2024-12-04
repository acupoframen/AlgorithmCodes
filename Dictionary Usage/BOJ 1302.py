from collections import defaultdict
n=int(input())
d=defaultdict(int)
for _ in range(n):
    temp=input()
    d[temp]+=1
answer=sorted(d.items(),key=lambda x:(-x[1],x[0]))

print(answer[0][0])