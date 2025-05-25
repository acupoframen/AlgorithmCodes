def func(k):
    if k==1:
        print("-",end="")
    else:
        func(k//3)
        print(" "*(k//3), end="")
        func(k//3)

while True:
    try:
        n=int(input())
        func(3**n)
        print()
    except:
        break