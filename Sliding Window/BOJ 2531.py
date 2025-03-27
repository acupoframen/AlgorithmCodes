from collections import  defaultdict
n,d,k,c=map(int,input().split())
data=list(int(input()) for _ in range(n))
data=data+data
sushis=[0 for _ in range(d+1)]
answer=0
count=0
sushis[c]=1e10
for i in range(k):
    if data[i]==c:
        continue
    if not sushis[data[i]]:
        count+=1
    sushis[data[i]]+=1
answer=count

for i in range(k,n+k):
    if data[i-k]!=c:
        sushis[data[i-k]]-=1
    if not sushis[data[i-k]]:
        count-=1
    if not sushis[data[i]]:
        count+=1
    sushis[data[i]]+=1
    answer=max(answer,count)
print(answer+1)