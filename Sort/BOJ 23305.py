n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
adata=[0 for _ in range(1000001)]
bdata=[0 for _ in range(1000001)]
for i in range(len(a)):
    adata[a[i]]+=1
for i in range(len(b)):
    bdata[b[i]]+=1
answer=0
l=0
for i in range(1000001):
    answer+=min(adata[i],bdata[i])
print(n-answer)