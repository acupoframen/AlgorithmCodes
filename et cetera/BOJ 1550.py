n=list(input())
answer=0
digit=1
while n:
    c=n[-1]
    if c=="A":
        c=10
    elif c=="B":
        c=11
    elif c=="C":
        c=12
    elif c=="D":
        c=13
    elif c=="E":
        c=14
    elif c=="F":
        c=15
    answer+=(int(c)*digit)
    digit*=16
    del n[-1]
print(answer)