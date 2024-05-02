a=int(input())
x=int(input())
def calc(a,x):
    if x==1:
        return a
    if x%2:
        return (a*(calc(a,x//2)%1000000007)**2)%1000000007
    else:
        return ((calc(a,x//2)%1000000007)**2)%1000000007
print(calc(a,x))