from collections import defaultdict
import math
n,g=input().split()
n=int(n)
d=defaultdict(int)
for _ in range(n):
    st=input()
    d[st]+=1
n=len(d)
if g=='Y':
    print(n)
elif g=='F':
    print(n//2)
elif g=='O':
    print(n//3)