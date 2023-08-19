t=int(input())
for _ in range(t):
    a, b= input().split()
    a=int(a)
    for i in range(len(b)):
        print(b[i]*a,end="")
    print("")