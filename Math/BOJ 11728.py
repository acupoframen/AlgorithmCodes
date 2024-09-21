n,m=map(int,input().split())
data1=list(map(int,input().split()))
data2=list(map(int,input().split()))
for i in data2:
    data1.append(i)
print(*sorted(data1))