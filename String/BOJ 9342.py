import re
t=int(input())
a=re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(t):
    n=input()
    if a.match(n)==None:
        print("Good")
    else:
        print("Infected!")