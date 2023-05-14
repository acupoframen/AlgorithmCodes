n=int(input())
a=input()
b=input()
if a[0]==b[0] and a[-1]==b[-1]:
    aList=sorted(list(a))
    bList=sorted(list(b))
    if aList==bList:
        aList=[]
        bList=[]
        for i in range(n):
            if a[i] in ['a','e','i','o','u']:
                pass
            else:
                aList.append(a[i])
            if b[i] in ['a','e','i','o','u']:
                pass
            else:
                bList.append(b[i])
        if aList==bList:
            print("YES")
            exit()

print("NO")