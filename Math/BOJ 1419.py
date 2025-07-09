l=int(input())
r=int(input())
k=int(input())
if k==2:
    print(max(0,r-2)-max(0,l-3))
elif k==3:
    print(max(0,r//3-1)-max(0,(l-1)//3-1))
elif k==4:
    ma=max(0,r//2-4)
    mi=max(0,(l-1)//2-4)
    if r>=12:
        ma-=1
    if l>=13:
        mi-=1
    print(ma-mi)
elif k==5:
    print(max(0,r//5-2)-max(0,(l-1)//5-2))