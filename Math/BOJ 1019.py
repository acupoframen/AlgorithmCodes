n=int(input())

answer=[0 for _ in range(10)]

k=1
start=1
def calculate(num, k):
    while num>0:
        answer[num%10]+=k
        num//=10

while start<=n:
    while n%10!=9:
        calculate(n,k)
        n-=1
    if n<start:
        break
    while start%10!=0:
        calculate(start,k)
        start+=1
    start//=10
    n//=10
    for i in range(10):
        answer[i]+=(n-start+1)*k
    k*=10

print(*answer)