n,m,k=map(int,input().split())
if n+1<m+k or n>m*k:
    print(-1)
    exit(0)
data=[1 for _ in range(m)]
if k==1:
    print(*[i for i in range(1,n+1)])
    exit(0)
a,b=(n-m) // (k-1) , (n-m) % (k-1)
for i in range(a):
    data[i]=k
if b>0:
    data[a]+=b
answer=[]
temp=0
for i in data:
    for j in range(temp+i,temp,-1):
        answer.append(j)
    temp+=i
print(*answer)