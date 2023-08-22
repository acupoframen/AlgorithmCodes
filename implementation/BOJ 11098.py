n=int(input())
for _ in range(n):
    p=int(input())
    maxval=0
    name=''
    for j in range(p):
        val, nam= input().split()
        if maxval<int(val):
            maxval=int(val)
            name=nam
    print(name)