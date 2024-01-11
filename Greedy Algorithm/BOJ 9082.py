t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,list(input())))
    shape=list(input())
    answer=0
    for i in range(n):        
        if i == 0:
            if data[0]!=0 and data[1]!=0:
                data[0]-=1
                data[1]-=1
                answer+=1
        elif i== n-1:
            if data[i]!=0 and data[i-1]!=0:
                data[i-1]-=1
                data[i-2]-=1
                answer+=1
        else:
            if data[i-1]!=0 and data[i]!=0 and data[i+1]!=0:
                data[i-1]-=1
                data[i]-=1
                data[i+1]-=1
                answer+=1
    print(answer)