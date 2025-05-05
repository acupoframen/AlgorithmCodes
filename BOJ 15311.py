data=list(0 for _ in range(2000))
data[0]=1
data[1]=1
for i in range(1,99):
    data[i+1]=data[i]+data[i-1]
print(data)
print(sum(range(100)))