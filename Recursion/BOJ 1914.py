n=int(input())
print(2**n-1)
answer=[]
def hanoi(a,b,c,count):
    if count==1:
        answer.append([a,b])
    else:
        hanoi(a,c,b,count-1)
        answer.append([a,b])
        hanoi(c,b,a,count-1)

if n<=20:
    hanoi(1,3,2,n)

    for i in answer:
        print(*i)