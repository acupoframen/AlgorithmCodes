n=int(input())
answer=[]
def hanoi (n,a,b,c):
    if n==1:
        answer.append([a,b])
    else:
        hanoi(n-1,a,c,b)
        answer.append([a,b])
        hanoi(n-1,c,b,a)

hanoi(n,1,3,2)
print(len(answer))
for a,b in answer:
    print(a,b)