n=int(input())
data=list(list(input()) for _ in range(n))
def func(x,y,num):
    if num==1:
        print(data[x][y],end="")
        return
    temp=data[x][y]
    halfnum=num//2
    for i in range(num):
        for j in range(num):
            if not data[x+i][y+j]==temp:
                print("(",end="")
                func(x,y,halfnum)
                func(x,y+halfnum,halfnum)
                func(x+halfnum,y,halfnum)
                func(x+halfnum,y+halfnum,halfnum)
                print(")",end="")
                return
    print(temp,end="")
    return

func(0,0,n)