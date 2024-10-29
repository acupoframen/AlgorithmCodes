n,l=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
protected=list(0 for _ in range(2001))
answer=0
for i in data:
    if not protected[i]:
        answer+=1
        for j in range(i,i+l):
            protected[j]=1
print(answer)