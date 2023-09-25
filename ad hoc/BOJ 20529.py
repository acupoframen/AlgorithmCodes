t=int(input())
for _ in range(t):
    n=int(input())
    data=list(input().split())
    if n>32:
        print(0)
    else:
        answer=1e10
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    temp=0
                    for l in range(4):
                        if data[i][l]!=data[j][l]:
                            temp+=1
                        if data[i][l]!=data[k][l]:
                            temp+=1
                        if data[j][l]!=data[k][l]:
                            temp+=1
                    
                    if temp<answer:
                        answer=temp
        print(answer)