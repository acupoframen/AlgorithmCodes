while True:
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    if a=='#' and b==0 and c==0:
        break
    if b<=17 and c<80:
        print(a,"Junior")
    else:
        print(a,"Senior")