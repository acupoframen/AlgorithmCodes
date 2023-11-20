import sys
input=sys.stdin.readline

a,b=input().split()
count=0
x,aval,bval=0,0,0
for i in range(2,37):
    try:
        atemp=int(a,i)
    except:
        continue
    for j in range(2,37):
        if i==j:
            continue
        try:
            btemp=int(b,j)
        except:
            continue

        if -2**63<=atemp<=2**63 and atemp==btemp:
            count+=1
            x=atemp
            aval=i
            bval=j

if count==1:
    print(x,aval,bval)
elif count==0:
    print("Impossible")
else:
    print("Multiple")