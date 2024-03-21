t=int(input())
for _ in range(t):
    input()
    n=int(input())
    temp=0
    for _ in range(n):
        temp+=int(input())
    if temp%n:
        print("NO")
    else:
        print("YES")