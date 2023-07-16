n,r,c=map(int,input().split())
answer=0
def calculate(x,y,n):
    global answer
    if x==r and y==c:
        print(answer)
        exit(0)
    if n==1:
        answer+=1
        return
    if not x<=r<x+n or not y<=c<y+n:
        answer+=n*n
        return
    halfn=n//2
    calculate(x,y,halfn)
    calculate(x,y+halfn,halfn)
    calculate(x+halfn,y,halfn)
    calculate(x+halfn,y+halfn,halfn)

calculate(0,0,2**n)
print(answer)