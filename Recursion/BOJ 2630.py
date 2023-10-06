n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
white=0
blue=0
def calc(x,y,size):
    global white, blue
    if size==1:
        if data[x][y]==1:
            blue+=1
        else:
            white+=1
        return
    currcolor=data[x][y]
    for i in range(size):
        for j in range(size):
            if currcolor!=data[x+i][y+j]:
                calc(x,y,size//2)
                calc(x+size//2,y,size//2)
                calc(x,y+size//2,size//2)
                calc(x+size//2,y+size//2,size//2)
                return
    if currcolor==1:
        blue+=1
    else:
        white+=1
    return
calc(0,0,n)
print(white)
print(blue)