u,v=input().split()
a=input()
b=input()
n=len(a)
resulta=0
resultb=0
for i in range(n):
    resulta=int(u)**int(a[i])
    resultb=int(v)**int(b[i])
    if resulta>resultb:
        print("ras")
        exit(0)
    elif resultb>resulta:
        print("auq")
        exit(0)
print("resauq")