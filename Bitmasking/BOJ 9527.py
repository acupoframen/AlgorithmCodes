a,b=map(int,input().split())

def calc(n):
    answer=0
    k=0
    while 2**k<=n:
        digit=2**(k+1)
        count=(n+1)//digit
        answer+=count*(digit//2)
        left=(n+1)%digit
        answer+=max(0,left-digit//2)
        k+=1
    return answer

print(calc(b)-calc(a-1))