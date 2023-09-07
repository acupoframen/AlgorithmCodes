t=int(input())
data=[[0], [1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for _ in range(t):
    a,b=map(int,input().split())
    if a%10 in [1,5,6]:
        
        print(data[a%10][0])
    elif a%10 in [2,3,7,8]:
        if not b%4:
            b=3
        else:
            b=b%4-1
            
        print(data[a%10][b])
    elif a%10==0:
        print(10)
    else:
        if b%2==0:
            print(data[a%10][1])

        else:
            print(data[a%10][0])