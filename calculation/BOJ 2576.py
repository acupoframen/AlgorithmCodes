data=[]
for i in range(7):
    n=int(input())
    if n%2:
        data.append(n)
if not len(data):
    print(-1)
else:
    print(sum(data))
    print(min(data))
