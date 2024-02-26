number=1
while True:
    l,p,v=map(int,input().split())
    if (l,p,v)==(0,0,0):
        break
    answer=0
    r=v%p
    if l<r:
        r=l
    answer=(v//p)*l+r
    print("Case {}: {}".format(number, answer))
    number+=1
    