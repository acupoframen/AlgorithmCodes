n,m=map(int,input().split())
data=list(map(int,input().split()))
for _ in range(m):

    i,j,k=map(int,input().split())
    temp=data[i-1:j]
    temp.sort()
    print(temp[k-1])