from collections import defaultdict
n,p,q=map(int,input().split())
dic=defaultdict(int)
dic[0]=1
def f(num):
    i,j=num//p,num//q
    if dic[num]!=0:
        return dic[num]
    dic[num]=f(num//p)+f(num//q)
    return dic[num]

print(f(n))