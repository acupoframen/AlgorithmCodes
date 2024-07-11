import math
while 1:
    n=int(input())
    if not n:
        break
    if n==1:
        print(0)
        continue
    k=n
    answer=k
    for i in range(2,math.ceil(n**0.5)+1):
        if not k%i:
            answer=answer-answer//i
            while not k%i:
                k/=i
    if k>1:
        answer=answer-answer/k
    print(int(answer))