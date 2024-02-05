n=int(input())
answer=n
i=2
while pow(i,2) <= n:
    if not n%i:
        while not n%i:
            n//=i
        answer-= answer//i
    i+=1
if n>1:
    answer-= answer//n
print(answer)