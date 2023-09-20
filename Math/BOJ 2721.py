t=int(input())
data=[0]
for i in range(1,302):
    data.append((i*(i+1))//2)
for _ in range(t):
    n=int(input())
    answer=0
    for i in range(1,n+1):
        answer+=(data[i+1]*i)
    print(answer)