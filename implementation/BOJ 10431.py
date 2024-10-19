p=int(input())
for _ in range(p):
    data=list(map(int,input().split()))[1:]
    answer=0
    for i in range(20):
        for j in range(i):
            if data[j]>data[i]:
                temp=data[i]
                data.remove(temp)
                data.insert(j,temp)
                answer+=i-j
                break
    print(_+1,answer)