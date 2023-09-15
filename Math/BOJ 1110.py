n=int(input())
i=1
a=n//10
b=n%10
while True:
    newval=(a+b)%10
    a=b
    b=newval
    if n==a*10+b:
        break
    i+=1
    
print(i)