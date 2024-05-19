n=int(input())
data=list(0 for _ in range(n+1))
for i in range(n*(n-1)//2):
    a,b,c,d=map(int,input().split())
    if c<d:
        data[b]+=3
    elif c>d:
        data[a]+=3
    else:
        data[a]+=1
        data[b]+=1

answer=sorted(data[1:],reverse=True)

for i in range(1,n+1):
    print(1+answer.index(data[i]))
