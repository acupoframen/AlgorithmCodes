t=int(input())
for _ in range(t):
    s=int(input())
    n=int(input())
    for i in range(n):
        temp=list(map(int, input().split()))
        s+=temp[0]*temp[1]
    print(s)