mw,ma=map(int,input().split())
tw,tb=map(int,input().split())
pw,pb=map(int,input().split())
a=min(mw,tb,pw)
b=min(ma,tw,pb)
if a>b:
    print(2*b+1)
elif a==b:
    print(a+b)
else:
    print(2*a+1)