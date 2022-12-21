def factorization(n):
    d=2
    factors=[]
    while d<=int(n**0.5)+1:
        if not n%d:
            factors.append(d)
            n/=d
        else:
            d+=1
    return factors

a,b=map(int,input().split())
aList,bList=[a,1],[b,1]
for i in factorization(a):
    aList.append(a//i)
    a/=i
for i in factorization(b):
    bList.append(b//i)
    b/=i
aList=list(map(int,aList))
bList=list(map(int,bList))
print(max(list(set(aList)&set(bList))))
