n=int(input())
length=len(str(n))
fa=[]
flag=0
while n>=0:
    newN=(length*n//(10**(length-1)))
    if newN in fa:
        flag=1
        print('FA')
        break
    else:
        n=length*(n//(10**(length-1)))
        length=len(str(n))
        fa.append(newN)
if not flag:
    print('NFA')
