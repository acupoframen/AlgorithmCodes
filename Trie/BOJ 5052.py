t=int(input())
for _ in range(t):
    n=int(input())
    data=list(input() for _ in range(n))
    data.sort()
    answer=1
    for i in range(n-1):
        temp=len(data[i])
        if data[i]==data[i+1][:temp]:
            answer=0
            print("NO")
            break
    if answer:
        print("YES")