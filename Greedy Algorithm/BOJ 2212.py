n=int(input())
k=int(input())
data=list(map(int,input().split()))

data.sort()
dataminus=[]
if k>=n:
    print(0)
    exit(0)
for i in range(n-1):
    dataminus.append(data[i+1]-data[i])
dataminus.sort(reverse=True)
print(sum(dataminus[k-1:]))