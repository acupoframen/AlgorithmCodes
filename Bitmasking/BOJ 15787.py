import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(0 for _ in range(n))
for _ in range(m):
    op=list(map(int,input().split()))
    if op[0]==1:
        i,x=op[1]-1,op[2]-1
        data[i]=data[i] | 1<<x
    elif op[0]==2:
        i,x=op[1]-1,op[2]-1
        data[i]=data[i] & ~(1<<x)
    elif op[0]==3:
        i=op[1]-1
        data[i]= data[i] <<1
        data[i]= data[i] & ~(1<<20)
    else:
        i=op[1]-1
        data[i]=data[i]>>1

print(len(set(data)))