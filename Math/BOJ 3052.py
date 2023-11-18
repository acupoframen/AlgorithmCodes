data=[0 for _ in range(42)]
for _ in range(10):
    a=int(input())
    data[a%42]=1

print(sum(data))