import sys
sys.setrecursionlimit(1000000)
data=[1e10]*1000001
n=int(input())
def fi(n):
    if n<=1:
        return n
    a,b=0,0
    if data[n-1]!=1e10:
        a=data[n-1]
    else:
        a=fi(n-1)
    if data[n-2]!=1e10:
        b=data[n-2]
    else:
        fi(n-2)
    return a+b
print(fi(n)%1000000007)