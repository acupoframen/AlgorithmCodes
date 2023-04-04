t=int(input())
data=[0 for _ in range(101)]
data[1:6]=[1,1,1,2,2]
for i in range(6,101):
    data[i]=data[i-5]+data[i-1]
for _ in range(t):
    n=int(input())
    print(data[n])