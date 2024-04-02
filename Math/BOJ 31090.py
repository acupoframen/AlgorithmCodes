t=int(input())
for _ in range(t):
    n=input()
    if n[2:]!='00':
        if (int(n)+1) % int(n[2:]):
            print("Bye")
        else:
            print("Good")
    else:
        print("Bye")