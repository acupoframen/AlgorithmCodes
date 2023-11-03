s,k,h=map(int,input().split())
if s+k+h>=100:
    print("OK")
else:
    if s==sorted([s,k,h])[0]:
        print("Soongsil")
    elif k==sorted([s,h,k])[0]:
        print("Korea")
    else:
        print("Hanyang")