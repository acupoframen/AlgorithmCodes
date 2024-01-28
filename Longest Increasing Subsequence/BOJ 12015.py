import bisect
n=int(input())
data=list(map(int,input().split()))
lis=[0]
for i in data:
    if lis[-1]<i:
        lis.append(i)
    else:
        lis[bisect.bisect_left(lis,i)]=i
print(len(lis)-1)