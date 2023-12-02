a,b=map(int,input().split())
a,b=max(a,b),min(a,b)
while a%b>0:
    a,b=b,a%b
    

print("".join('1'*b))