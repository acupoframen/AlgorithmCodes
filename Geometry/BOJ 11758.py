def calc(a,b,c):
    temp=(a[0]*b[1])+(b[0]*c[1])+(c[0]*a[1])
    temp-=(a[1]*b[0])+b[1]*c[0]+c[1]*a[0]
    if temp>0:
        return 1
    elif not temp:
        return 0
    return -1
data=list(list(map(int,input().split())) for _ in range(3))
print(calc(*data))