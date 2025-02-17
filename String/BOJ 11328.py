n=int(input())
for _ in range(n):
    a,b=input().split()
    if sorted(list(a))==sorted(list(b)):
        print("Possible")
    else:
        print("Impossible")