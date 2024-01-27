import sys
sys.setrecursionlimit(int(1e5))
n=int(input())
dict={}
dict[0]=0
dict[1]=1
dict[2]=1
mod=1000000007
def fibo(n):
    if n not in dict:
        if n%2==1:
            a=fibo(n//2)
            b=fibo(n//2+1)
            answer=((a)**2+(b)**2)%mod
        else:
            a=fibo(n//2)
            b=fibo(n//2-1)
            answer=((a)*(a+2*(b)))%mod
        dict[n]=answer
    return dict[n]
print(fibo(n))