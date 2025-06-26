data=list(map(int, input().split()))
data.sort()
if data[0]+data[1]<=data[2]:
    data[2]=data[0]+data[1]-1
print(sum(data))