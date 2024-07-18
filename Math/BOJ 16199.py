a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
if b<e:
    print(d-a)
elif b==e:
    if f>=c:
        print(d-a)
    else:
        print(d-a-1)
else:
    print(d-a-1)
temp=d-a+1
print(temp)
print(temp-1)