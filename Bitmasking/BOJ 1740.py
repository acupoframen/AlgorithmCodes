n=int(input())
n=str(bin(n))[2:][::-1]
answer=0
exp=1
for i in n:
    answer+=int(i)*exp
    exp*=3
print(answer)