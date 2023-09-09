import math
def factorize(n):
    sieve = [True] * int(n ** 0.5 + 2)
    
    for x in range(2, int(len(sieve) ** 0.5 + 2)):
        if not sieve[x]: 
            continue
        for i in range(x * x, len(sieve), x):
            sieve[i] = False

    factors = []
    for i in range(2, len(sieve)):
        if i * i > n:
            break
        if not sieve[i]:
            continue
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

n=int(input())
factors=factorize(n)
answerfactor=[]
for i in range(len(factors)):
    answerfactor.append(factors[i])
if n==2:
    print(3)
    exit(0)
elif n==3:
    print(5)
    exit(0)

from functools import cmp_to_key

def solution(numbers):
    answer = ''
    def compare(a, b):
        a = str(a)
        b = str(b)
        s1 = int(a + b)
        s2 = int(b + a)
        if s1 < s2:
            return 1
        elif s1 > s2:
            return -1
        else:
            return 0
    numbers.sort(key=cmp_to_key(compare))
    answer = str(int("".join(map(str, numbers))))
    return answer
answer=int(solution(answerfactor))
count=1
answercount=0
while True:
    if n>2*count:
        count*=2
        answercount+=1
    else:
        break
count1=3
answercount1=1
while True:
    if n>2*count1:
        count1*=2
        answercount1+=1
    else:
        break
if answercount1>=answercount:
    number='3'+'2'*(answercount1-1)
    answer+=int(number)
else:
    number='2'*answercount
    answer+=int(number)

print(answer)