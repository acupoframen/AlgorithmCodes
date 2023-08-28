def factorial(n):
    if n==0:
        return 1
    elif n!=1:
        return factorial(n-1)*n
    return n
n,k=map(int,input().split())
print(factorial(n)//factorial(k)//factorial(n-k))
