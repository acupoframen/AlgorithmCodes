n=int(input())
data=[0 for _ in range(2000)]
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a+180-b,a+180+b+1):
        data[i%360]=1
print(data.count(1))