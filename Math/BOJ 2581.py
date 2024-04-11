sieve=[1 for _ in range(10001)]
for i in range(2,101):
    if sieve[i]:
        for j in range(2*i,10001,i):
            sieve[j]=0

sieve[1]=0
n=int(input())
m=int(input())
answer1=0
answer2=0
for i in range(n,m+1):
    if sieve[i]:
        if not answer1:
            answer1=i
        answer2+=i
if not answer1:
    print(-1)
    exit(0)
print(answer2)
print(answer1)