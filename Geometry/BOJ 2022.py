x,y,c=map(float,input().split())
left=0
right=(min(x,y)**2-c**2)**0.5
while left<=right:
    mid=(left+right)/2
    xheight=(x**2-mid**2)**0.5
    yheight=(y**2-mid**2)**0.5
    val=c/xheight+c/yheight
    if 0.999<val<1.001:
        print(mid)
        break
    if val>1:
        right=mid
    else:
        left=mid