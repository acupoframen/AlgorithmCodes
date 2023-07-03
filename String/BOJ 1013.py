import re
import sys
input=sys.stdin.readline
t=int(input())
p=re.compile('(100+1+|01)+')
for _ in range(t):
    num=input().strip()
    if p.fullmatch(num):
        print("YES")
    else:
        print("NO")