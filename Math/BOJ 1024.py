n,l=map(int,input().split())
for i in range(l,101):
    if n//i-i//2+1<0:
        break
    if i%2: #Odd
        if not n%i:
            for j in range(n//i-i//2,n//i+i//2+1):
                print(j, end=" ")
            exit(0)
    else: #even
        if (n//i+n//i+1)*i//2==n:
            for j in range(n//i-i//2+1,n//i+i//2+1):
                print(j, end=" ")
            exit(0)
print(-1)