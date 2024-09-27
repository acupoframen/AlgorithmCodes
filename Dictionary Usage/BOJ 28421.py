from collections import defaultdict
import sys
input=sys.stdin.readline
n,q=map(int,input().split())
import math
data=[1e10]+list(map(int,input().split()))
dic=defaultdict(list)
for i in range(1,n+1):
    dic[data[i]].append(i)
for _ in range(q):
    a,b=map(int,input().split())
    if n==1 and a==1:
        print(0)
        continue
    if a==1:
        if b==0:
            if len(dic[0])>0:
                print(1)
            else:
                print(0)
            continue
        flag=0
        for i in range(1,1+int(math.sqrt(b))):
            if i*i==b:
                if len(dic[i])>1:
                    flag=1
                break
            elif not b%i and len(dic[i])>0 and len(dic[b//i]):

                flag=1
                break
        if flag:
            print(1)
        else:
            print(0)
    else:
        del dic[data[b]][dic[data[b]].index(b)]
        data[b]=0
        dic[0].append(b)