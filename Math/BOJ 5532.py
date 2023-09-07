l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if not a%c:
    a=a//c
else:
    a=a//c+1
if not b%d:
    b=b//d
else:
    b=b//d+1
print(l-max(a,b))