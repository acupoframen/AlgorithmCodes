a=int(input())
b=int(input())
c=int(input())
answer=str(a*b*c)
data=[0 for _ in range(10)]
for i in answer:
    data[int(i)]+=1

for i in data:
    print(i)