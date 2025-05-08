t=int(input())
for _ in range(t):
    n=int(input())
    temp=0
    i=2
    while i<=n:
        temp+=n//i
        i*=2
    temp1=0
    i=5
    while i<=n:
        temp1+=n//i
        i*=5
    answer=min(temp1,temp)
    print(answer)