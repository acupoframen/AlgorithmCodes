n,new,p=list(map(int,input().split()))
if n==0:
    print(1)
    exit(0)
data=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    if i>p:
        break
    if new>=data[i]:
        if new==data[-1] and len(data)>p:
            print(-1)
        else:
            print(i)
        exit(0)
if len(data)<=p:
    print(len(data))
else: print(-1)