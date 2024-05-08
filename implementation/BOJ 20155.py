from collections import defaultdict
n,m=map(int,input().split())
data=list(map(int,input().split()))
answer=defaultdict(int)
for i in data:
    answer[i]+=1

val=0
for i in answer.values():
    val=max(val,i)
print(val)