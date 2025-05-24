from collections import defaultdict
n=int(input())
data=defaultdict(int)
answer=0
for i in range(n):
    s=input()
    if s=='ENTER':
        data=defaultdict(int)
        continue
    if data[s]==0:
        data[s]=1
        answer+=1
print(answer)