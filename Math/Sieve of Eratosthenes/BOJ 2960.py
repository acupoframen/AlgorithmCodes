n,k=map(int,input().split())
data=list(1 for _ in range(n+1))
for i in range(2,n+1):
    if data[i]:
        for j in range(i,n+1,i):
            if data[j]:
                data[j]=0
                k-=1
                if not k:
                    print(j)
                    exit(0)