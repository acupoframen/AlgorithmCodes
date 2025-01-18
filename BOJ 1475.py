n=input()
data=[0 for _ in range(10)]
for i in n:
    if i=='6':
        data[9]+=1
    else:
        data[int(i)]+=1
if data[9]%2:
    data[9]//=2
    data[9]+=1
else:
    data[9]//=2
print(max(data))
