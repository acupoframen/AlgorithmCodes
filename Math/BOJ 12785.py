from math import comb
mod=1000007
w,h=map(int,input().split())
x,y=map(int,input().split())
temp=comb(x-1+y-1,x-1)
temp*=comb(w-x+h-y,w-x)
print(temp%mod)