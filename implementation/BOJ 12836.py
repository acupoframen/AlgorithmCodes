n,q=map(int,input().split())
data=[0 for _ in range(10001)]
for _ in range(q):
    a,p,x=map(int,input().split())
    if a==1:
        data[p]+=x
    else:
        print(sum(data[p:x+1]))