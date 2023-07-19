import sys
from collections import deque
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline
data=[]
while True:
    try:
        data.append(int(input()))
    except:
        break
def calc(a,b):
    if a>b:
        return
    else:
        root=data[a]
        half=b+1
        for i in range(a+1,b+1):
            if root<data[i]:
                half=i
                break
        calc(a+1,half-1)
        calc(half,b)
        print(root)
if data:
    calc(0,len(data)-1)