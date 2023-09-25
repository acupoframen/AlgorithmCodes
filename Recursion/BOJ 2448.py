n=int(input())
data=[[' ' for _ in range (n*2)] for _ in range(n)]

def func(x,y,val):
    if val<=3:
        for i in range(3):
            for j in range(i+1):
                data[x+i][y+j]='*'
                data[x+i][y-j]='*'
        data[x+1][y]=' '
        return

    func(x,y,val//2)
    func(x+val//2,y-val//2,val//2)
    func(x+val//2,y+val//2,val//2)

func(0,n-1,n)

for i in range(n):
    print("".join(data[i]))