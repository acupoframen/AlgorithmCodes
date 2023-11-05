n,m=map(int,input().split())
data=list(map(int,(input().split())))
pos=[]
neg=[]
for i in range(n):
    if data[i]>0:
        pos.append(data[i])
    else:
        neg.append(data[i])

pos.sort(reverse=True)
neg.sort()
dist=[]
for i in range(len(neg)//m):
    dist.append(abs(neg[m*i]))
if len(neg)%m!=0:
    dist.append(abs(neg[m*(len(neg)//m)]))
for i in range(len(pos)//m):
    dist.append(pos[m*i])
if len(pos)%m!=0:
    dist.append(pos[m*(len(pos)//m)])

answer=0
dist.sort()
answer=dist.pop()
answer+=(sum(dist)*2)
print(answer)