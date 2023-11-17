n=int(input())
length=[0 for _ in range(10001)]
data=list(map(int,input().split()))

for i in data:
    if length[i]==1:
        length[i]=2
    elif length[i]==0:
        length[i]=1
print(sum(length))